
class Word_search_solver():
    def __init__(self):
        self.instances_of_xmas = 0
        
    def part_one(self,matrix) -> int:
        storage_array = [[Letter_rating(0,0,0) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for y_val in range(len(matrix)):
            left_right_counter = 0
            for x_val in range(len(matrix[0])):
                current_letter = matrix[y_val][x_val]                
                #update row counter
                #update right diagonal

                if self.get_next_letter(left_right_counter) == current_letter:
                    left_right_counter = self.get_next_counter(left_right_counter)
                else:
                    left_right_counter = 0 

                right_diagonal = self.check_val(x_val -1,y_val -1,current_letter,storage_array,"right_diagonal")
                vertical = self.check_val(x_val,y_val -1,current_letter,storage_array,"vertical")
                left_diagonal = self.check_val(x_val +1,y_val -1,current_letter,storage_array,"left_diagonal")

                if current_letter == 'S': #if we end a word, we restart everything
                    right_diagonal = -1
                    vertical = -1
                    left_diagonal = -1
                    left_right_counter = -1
                
                if current_letter == "X": #if we begin a word, we restart everything
                    right_diagonal = 1
                    vertical = 1
                    left_diagonal = 1
                    left_right_counter = 1

                storage_array[y_val][x_val] = Letter_rating(right_diagonal,vertical,left_diagonal)


        return self.instances_of_xmas
                #-1 except this letter
                #update vert
                #update left diagonal
    
    def check_val(self,y_val,x_val,current_letter,storage_matrix,kind):
        if x_val < 0 or x_val > len(storage_matrix)-1 or y_val < 0 or y_val > len(storage_matrix)-1:
            return 0
        if kind == "left_diagonal":
            kind_prev = storage_matrix[x_val][y_val].left_diagonal
        if kind == "vertical":
            kind_prev = storage_matrix[x_val][y_val].vertical
        if kind == "right_diagonal":
            kind_prev = storage_matrix[x_val][y_val].right_diagonal
        if self.get_next_letter(kind_prev) == current_letter:
            return self.get_next_counter(kind_prev)
        return 0

    #checks to letters to see if the would form and xmas
    def check_string(self,char1,char2) -> bool:
        if char1 == 'M' and char2 == 'S':
            return True
        if char1 == 'S' and char2 == 'M':
            return True
        return False

    def part_two(self,matrix):
        count = 0
        for y_val in range(len(matrix)):
            for x_val in range(len(matrix[0])):
                if y_val == 0 or x_val == 0: #
                    continue
                if matrix[y_val][x_val] == 'A':
                    try: #catching index errors
                        if self.check_string(matrix[y_val-1][x_val-1],matrix[y_val+1][x_val+1]) and \
                            self.check_string(matrix[y_val-1][x_val+1],matrix[y_val+1][x_val-1]):
                            count += 1
                            if not self.double_check(matrix[y_val-1][x_val-1],matrix[y_val][x_val],matrix[y_val+1][x_val+1]):
                                print("Fail")
                            if not self.double_check(matrix[y_val-1][x_val+1],matrix[y_val][x_val],matrix[y_val+1][x_val-1]):
                                print("Fail")
                    except IndexError:
                        continue
        return count
    
    def double_check(self,char1,char2,char3):
        val = char1 + char2 + char3
        if val == "MAS" or val == "SAM":
            return True
        return False

                

    

    def get_next_letter(self,prev_code_value:int):  #what if 4, what if 0 
        reference = "XMAS" 
        #1 is the code for the first letter in xmas x, -1 is the code of the first letter in samx, s
        if prev_code_value == 0:
            return "Q"
        if prev_code_value < 0:
            return reference[prev_code_value -1]
        
        if prev_code_value > 0:
            return reference[prev_code_value]
        
    def get_next_counter(self,counter:int): # -2 -> -3, # 2 -> 3
        # 4 -> -1, -4 ->1 (update total_counter)
        # if counter == 0: #if it didn't
        #     return 0
        if abs(counter) >= 3:
            self.instances_of_xmas += 1
        if counter < 0:
            return counter - 1
        return counter + 1


class Letter_rating():
    def __init__(self,right_diagonal,vertical,left_diagonal):
        #for each of these we will record the largest
        #word it could be apart of. 0 for not, +1-4 if xmas
        #-1--4 for samx.
        self.left_diagonal = left_diagonal 
        self.vertical = vertical
        self.right_diagonal = right_diagonal


def get_puzzle_input():
    matrix = []
    with open('day_4.txt','r') as file:
        line = file.readline()
        while line != "":
            new_row = []
            for char in line:
                new_row.append(char)
            matrix.append(new_row)
            line = file.readline()
            
    return matrix

def part_one():
    matrix = get_puzzle_input()
    w = Word_search_solver()
    print(w.part_one(matrix))

def part_two():
    matrix = get_puzzle_input()
    w = Word_search_solver()
    print(w.part_two(matrix))



if __name__ == "__main__":
    #print(get_puzzle_input())
    #part_one()
    part_two()