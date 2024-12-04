# get input
import re


input_matrix = []


with open("day_2.txt",'r') as input:
    row = input.readline()
    while row != None and row != "":
        final_row = []
        string_numbers = re.findall("[0-9]+",row)
        for number in string_numbers:
            final_row.append(int(number))
        input_matrix.append(final_row)
        row = input.readline()


def part_one(data:list) ->int:
    safe_levels = 0
    for report in data:
        if level_checker(report):
            safe_levels += 1
    return safe_levels

def level_checker(report:list) -> bool:
    # find up or down first
    dif = report[0] - report[1] # if postive, going up, #if negative,going down
    if dif < 0:
        sign = -1
    elif dif > 0:
        sign = 1
    else:
        return False
    for l_index in range(len(report) - 1): #check < 3 dif, in right direction
        diff = report[l_index] - report[l_index +1]
        if abs(diff) > 3 or abs(diff) < 1: 
            return False
        #diff and sign need to be either both negative or both positve
        if sign * diff < 0:
            return False
        
    return True



def part_two(data:list) -> int:
    safe_levels = 0
    for report in data:
        if safe_level_checker(report):
            safe_levels += 1
            if not level_checker(report):
                print("safe_level",report)
    return safe_levels
        
def level_checker_helper(report:list,sign) -> bool:
    # find up or down first
    for l_index in range(len(report) - 1): #check < 3 dif, in right direction
        if not checks_two_values(report[l_index],report[l_index+1],sign):
            return False
    return True

def safe_level_checker(report:list):
    # find up or down first
    sign = 0
    for num_index in range(4):
        temp = report[num_index] - report[num_index + 1]
        if temp > 0:
            sign += 1
        if temp < 0:
            sign += -1
    if sign > 0:
        sign = 1 #safe_level 
    elif sign < 0:
        sign = -1
    else:
        return False
    print("sign", sign) 
    for l_index in range(len(report) - 1): #check < 3 dif, in right direction
        if not checks_two_values(report[l_index],report[l_index + 1],sign):
            print(report[l_index],report[l_index + 1])
            try:
                if checks_two_values(report[l_index],report[l_index + 2],sign) or checks_two_values(report[l_index +1],report[l_index + 2],sign):
                    print(checks_two_values(report[l_index],report[l_index + 2],sign))
                    print(checks_two_values(report[l_index +1],report[l_index + 2],sign))
                    return level_checker_helper(report[l_index+1:],sign)
                return False
            except IndexError:
                #print(f"error on index {l_index},{l_index + 2}",report)
                return True
 # [# #] # 
    return True
        
def checks_two_values(val1,val2,sign) -> bool:
    diff = val1 - val2
    if abs(diff) > 3 or abs(diff) < 1: 
        return False
    if sign * diff < 0: #diff and sign need to be either both negative or both positve
        return False
    return True
#check first 2 numbers up or down
#check also within 3

#subsequent going same as first 2
#check abs dif < 3

# print(part_two(input_matrix))

# test_level = [9, 7, 6, 2, 1]
# print(safe_level_checker(test_level))

checks_two_values(7,5,1)
checks_two_values(5,7,1)
checks_two_values(5,7,-1)
checks_two_values(7,5,-1)
checks_two_values(9,5,-1)
checks_two_values(3,8,1)

# print(level_checker_helper(test_level))

# test2 = [32, 36, 36, 38, 45]
test3 = [38, 45, 48, 49, 52, 53, 54, 54]

test4 = [45, 48, 49, 52, 53, 54, 54]

test5 = [31, 32, 30, 33, 34, 37]
print(safe_level_checker(test5))
#print("final verdict",safe_level_checker(test3))
