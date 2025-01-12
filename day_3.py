import re

def main():
    input_string = ""
    with(open("day_3.txt",'r')) as message:
        string = message.readline()
        while string != None and string != "":
            input_string += string
            string = message.readline()

    print(part_one(input_string))
    print(part_two(input_string))
    #print(jen_part_two(input_string))

def part_one(input:str):
    list_of_mult = re.findall("mul[(][0-9]+,[0-9]+[)]",input) #mul(num,num)
    sum = 0
    for mult in list_of_mult:
        nums = re.match("mul[(]([0-9]+),([0-9]+)[)]",mult)
        sum += int(nums.group(1)) * int(nums.group(2))
    return sum

def part_two(input: str):
    do_list = re.split("(do[(][)])|(don't[(][)])", input)
    status = True
    #have we encountered a do or don't
    sum = 0
    for ticket in do_list:
        if ticket == None:
            continue
        if ticket == "do()":
            status = True
        if ticket == "don't()":
            status = False
        if status: 
            sum += part_one(ticket)

    return sum

def jen_part_two(input:str) -> int:
    list_of_mult = re.findall("mul[(][0-9]+,[0-9]+[)]|do[(][)]|don't[(][)]",input)
    status = True
    sum = 0
    for ticket in list_of_mult:
        if ticket == "do()":
            status = True
        elif ticket == "don't()":
            status = False
        elif status: 
            nums = re.match("mul[(]([0-9]+),([0-9]+)[)]",ticket)
            sum += int(nums.group(1)) * int(nums.group(2))
    return sum
if __name__ == '__main__':
    main()