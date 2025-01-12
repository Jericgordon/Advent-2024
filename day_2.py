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
        if not checks_two_values(report[l_index],report[l_index +1],sign):
            return False
    return True


def brute_force_part_two(data:list):
    safe_levels = 0
    for report in data:
        if level_checker(report):
            safe_levels += 1
        else:
            if brute_force_helper(report):
                safe_levels += 1
    return safe_levels

def brute_force_helper(report:list):
    for level_index in range(len(report)):
        if level_checker(report[:level_index] +report[level_index +1:]):
            return True
    return False

def main():
    print(part_one(input_matrix))
    print(brute_force_part_two(input_matrix)) #558
    print(part_two(input_matrix)) #570

def part_two(data:list) -> int:
    safe_levels = 0
    for report in data:
        if safe_level_checker(report):
            safe_levels += 1
            if not level_checker(report) and not brute_force_helper(report):
                print("safe_level",report)
    return safe_levels
        
def level_checker_helper(report:list,sign) -> bool:
    # find up or down first
    for l_index in range(len(report) - 1): #check < 3 dif, in right direction
        if not checks_two_values(report[l_index],report[l_index+1],sign):
            return False
    return True

def find_sign(report_beginning:list):
    sign = 0
    for num_index in range(3):
        temp = report_beginning[num_index] - report_beginning[num_index + 1]
        if temp > 0:
            sign += 1
        if temp < 0:
            sign += -1
    if sign > 0:
        return 1
    elif sign < 0:
        return -1
    return 0

def safe_level_checker(report:list):
    # find up or down first
    sign = find_sign(report[:4])
    if sign == 0: #check to maek
        return False
    for l_index in range(len(report) - 1): #check < 3 dif, in right direction
        if not checks_two_values(report[l_index],report[l_index + 1],sign):
            try:
                if checks_two_values(report[l_index],report[l_index + 2],sign) or checks_two_values(report[l_index +1],report[l_index + 2],sign):
                    return level_checker_helper(report[l_index+1:],sign)
                return False
            except IndexError:
                return True 
    return True
        
def checks_two_values(val1,val2,sign) -> bool:
    diff = val1 - val2
    if abs(diff) > 3 or abs(diff) < 1: 
        return False
    if sign * diff < 0: #diff and sign need to be either both negative or both positve
        return False
    return True




#print(part_two(input_matrix))

main()