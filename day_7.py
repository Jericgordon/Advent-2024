import re

def importdoc(file_name:str):
    target_list = []
    values_list = []
    with open(file_name) as file:
        line = file.readline()
        while line != "":
            output = re.split(":",line)
            list = re.findall("[0-9]+",output[1])
            target_list.append(int(output[0]))
            values_list.append(list)
            line = file.readline()
    return target_list,values_list


#initial current sum should be the first element in the list. index starts at 0
#we want to take our current sum, and either add or multiply that by the index + 1th item
def recursive_operator_check(target:int,current_sum:int,index:int,val_list:list) -> bool:
    if target < current_sum: # if we're ever bigger than our target, we can prune the branch
        return False
    
     #if we get to the end of the list, and still are not at our target, we can return false
    if index == len(val_list) -1:
        if target == current_sum:
            return True
        return False
    
    #either add or multiply
    return recursive_operator_check(target,current_sum * int(val_list[index +1]),index + 1,val_list) or \
          recursive_operator_check(target,current_sum + int(val_list[index +1]),index + 1,val_list)


def concat(val1:int,val2:int) -> int:
    str1=str(val1)
    str2=str(val2)
    combined = str1 + str2
    return int(combined)

def part_one(file:str)->int:
    target_lists,values_list = importdoc(file)
    sum = 0
    for index in range(len(target_lists)):
        key = target_lists[index]
        value = values_list[index]
        if recursive_operator_check(key,int(value[0]),0,value):
            sum += key
    
    return sum


def recursive_three_operator_check(target:int,current_sum:int,index:int,val_list:list) -> bool:
    if target < current_sum: # if we're ever bigger than our target, we can prune the branch
        return False
    
     #if we get to the end of the list, and still are not at our target, we can return false
    if index == len(val_list) -1:
        if target == current_sum:
            return True
        return False
    
    #either add or multiply
    return recursive_three_operator_check(target,current_sum * int(val_list[index +1]),index + 1,val_list) or \
          recursive_three_operator_check(target,current_sum + int(val_list[index +1]),index + 1,val_list) or \
          recursive_three_operator_check(target,concat(current_sum,int(val_list[index +1])),index +1,val_list)


def part_two(file:str)->int:
    target_lists,values_list = importdoc(file)
    sum = 0
    for index in range(len(target_lists)):
        key = target_lists[index]
        value = values_list[index]
        if recursive_three_operator_check(key,int(value[0]),0,value):
            sum += key
    
    return sum

if __name__ == "__main__":
    #print(part_one("day_7.txt"))
    print(part_two("day_7.txt"))