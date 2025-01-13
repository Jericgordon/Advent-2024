import copy

def get_input(file_name:str) -> list:
    matrix = []
    with open(file_name,'r') as file:
        line = file.readline()
        while line != "":
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            matrix.append(row)
            line = file.readline()
    return matrix

def find_caret(matrix:list):
    for y_val in range(len(matrix)):
        for x_val in range(len(matrix[0])):
            if matrix[y_val][x_val] not in ['#','.']:
                print(matrix[y_val][x_val])
                return x_val,y_val



def next_step(x_val,y_val,caret):
    match(caret):
        case '^':
            return x_val,y_val -1
        case '>':
            return x_val + 1, y_val
        case 'v':
            return x_val,y_val +1
        case "<":
            return x_val - 1, y_val
        case _:
            raise(AttributeError("Illegal character"))

def rotate(caret):
    carets = ['^','>','v','<']
    index = carets.index(caret)
    return carets[(index + 1) % 4]




def advance_matrix(matrix:list,x_val,y_val):
    h_x,h_y = next_step(x_val,y_val,matrix[y_val][x_val]) #what is the next step she wants to take
    
    #Check and see if she's gone off the map
    if (h_y < 0 or h_y >= (len(matrix)) or h_x < 0 or h_x >= (len(matrix[0]))):
        matrix[y_val][x_val] = 'X'
        return matrix,-1,-1,True

    #check if we need to rotate the caret
    if matrix[h_y][h_x] == '#':
        matrix[y_val][x_val] = rotate(matrix[y_val][x_val])
        return matrix,x_val,y_val,False

    #otherwise advance and
    matrix[h_y][h_x] = matrix[y_val][x_val]
    matrix[y_val][x_val] = 'X'
    return matrix,h_x,h_y,False

def part_one(file_name:str):
    matrix = get_input(file_name)
    x_val,y_val = find_caret(matrix)
    done = False
    while not done:
        matrix,x_val,y_val,done = advance_matrix(matrix,x_val,y_val)
        

    return count_xs(matrix)

def count_xs(matrix:int):
    count = 0
    for y_val in range(len(matrix)):
        for x_val in range(len(matrix[0])):
            if matrix[y_val][x_val] == 'X':
                count += 1
    return count

def part_two(file_name:str):
    matrix = get_input(file_name)
    x_val,y_val = find_caret(matrix)
    orig_x_val,orig_y_val = find_caret(matrix)
    original_caret = matrix[y_val][x_val]
    done = False
    while not done:
        matrix,x_val,y_val,done = advance_matrix(matrix,x_val,y_val)
    loops = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "X":
                print(y,x)
                test_matrix = copy.deepcopy(matrix)
                test_matrix[y][x] = "#"
                test_matrix[orig_y_val][orig_x_val] = original_caret
                if infinite_loop(test_matrix,orig_x_val,orig_y_val):
                    loops +=1
    return loops

    

def infinite_loop(matrix,x_val,y_val):
    done = False
    seen = {}
    while not done:
        matrix,x_val,y_val,done = advance_matrix(matrix,x_val,y_val)
        if (x_val,y_val) not in seen:
            seen[(x_val,y_val)] = [matrix[y_val][x_val]]
            continue
        current_list = seen[(x_val,y_val)]
        if matrix[y_val][x_val] in current_list:
            return True
        else:
            seen[(x_val,y_val)].append(matrix[y_val][x_val])
    return False
        



    
if __name__ == '__main__':
    print("part 1: ",part_one("day_6.txt"))
    print("part 2: ",part_two("day_6.txt"))