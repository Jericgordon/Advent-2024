

def import_map(file_name:str) -> list:
    return_array = []
    with open(file_name) as file:
        line = file.readline()
        while line != "":
            return_array.append(line)
            line = file.readline()
    
    return return_array


def get_dict_of_locations(array:list) -> dict:
    ret_dict = {}
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] != '.' and array[y][x] != '\n':
                if array[y][x] in ret_dict:
                    ret_dict[array[y][x]].append((y,x))
                else:
                    ret_dict[array[y][x]] = [(y,x)]
    return ret_dict

def in_range(point:tuple,bound:tuple) ->bool:
    if point[0] < 0 or point[0] >bound[0]:
        return False
    if point[1] < 0 or point[1] >bound[0]:
        return False
    return True

# 3,2   5,6
def find_antinodes(p_1:tuple,p_2:tuple) -> list:
    y_dif = p_1[0] - p_2[0]
    x_dif = p_1[1] - p_2[1]
    antinode_1 = (p_1[0] + y_dif,p_1[1] + x_dif)
    antinode_2 = (p_2[0] - y_dif,p_2[1] - x_dif)
    return [antinode_1,antinode_2]


def get_nodes(list_of_points:list,bounds:tuple)-> list:
    list_of_antinodes = []
    for p_i in range(len(list_of_points)):
        for c_p in range(p_i,len(list_of_points)):
            if p_i == c_p: #don't compare a point with itself
                continue
            antinodes = find_antinodes(list_of_points[p_i],list_of_points[c_p])
            #check to see if the antinodes are in bounds
            for node in antinodes:
                if in_range(node,bounds) and node not in list_of_antinodes:
                    #print(node)
                    list_of_antinodes.append(node)  
    return list_of_antinodes

def part_one(file_name:str) -> int:
    map = import_map(file_name)
    dictionary_for_points = get_dict_of_locations(map)
    print(dictionary_for_points)
    y_len = len(map) 
    x_len = len(map[0]) 

    list_of_antinodes = []
    for key,value in dictionary_for_points.items():
        for node in get_nodes(value,(y_len,x_len)):
            if node not in list_of_antinodes:
                list_of_antinodes.append(node)
    return len(list_of_antinodes)

def part_two(file_name:str) -> int:
    map = import_map(file_name)
    dictionary_for_points = get_dict_of_locations(map)
    print(dictionary_for_points)
    y_len = len(map) -1
    x_len = len(map[0]) -1

    list_of_antinodes = []
    for key,value in dictionary_for_points.items():
        for node in get_all_nodes(value,(y_len,x_len)):
            if node not in list_of_antinodes:
                list_of_antinodes.append(node)
        for node in value:
            if len(value) > 1 and value not in list_of_antinodes:
                list_of_antinodes.append(node)
    for y in range(y_len +1):  #debug print
        str = ""
        for x in range(x_len):
            if (y,x) in list_of_antinodes:
                str += "#"
            else:
                str += "."
        print(str)
    final_filter = []
    for item in list_of_antinodes:
        if item not in final_filter:
            final_filter.append(item)

    
    return len(final_filter)
        
def get_all_nodes(list_of_points:list,bound:tuple)-> list:
    list_of_antinodes = []
    for p_i in range(len(list_of_points)):
        for c_p in range(p_i,len(list_of_points)):
            if p_i == c_p: #don't compare a point with itself
                continue
            antinodes = find_all_antinodes(list_of_points[p_i],list_of_points[c_p],bound)
            #check to see if the antinodes are in bounds
            for node in antinodes:
                if node not in list_of_antinodes:
                    list_of_antinodes.append(node)  
    return list_of_antinodes

def find_all_antinodes(p_1:tuple,p_2:tuple,bound:tuple) -> list:
    list_of_nodes = []
    y_dif = p_1[0] - p_2[0]
    x_dif = p_1[1] - p_2[1]
    antinode_1 = (p_1[0] + y_dif,p_1[1] + x_dif)
    while in_range(antinode_1,bound):
        list_of_nodes.append(antinode_1)
        antinode_1 = (antinode_1[0] + y_dif,antinode_1[1] + x_dif)
    antinode_2 = (p_2[0] - y_dif,p_2[1] - x_dif)
    while in_range(antinode_2,bound):
        list_of_nodes.append(antinode_2)
        antinode_2 = (antinode_2[0] - y_dif,antinode_2[1] - x_dif)
    return list_of_nodes

if __name__ == "__main__":
    print(part_one("day_8.txt"))
    print(part_two("day_8.txt"))
