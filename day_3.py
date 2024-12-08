import re

def main():
    input_string = ""
    with(open("day_3.txt",'r')) as message:
        string = message.readline()
        while string != None and string != "":
            input_string += string
            string = message.readline()

    #print(part_one(input_string))

def part_one(input:str):
    list_of_mult = re.findall("mul[(][0-9]+,[0-9]+[)]",input) #mul(num,num)
    sum = 0
    for mult in list_of_mult:
        nums = re.match("mul[(]([0-9]+),([0-9]+)[)]",mult)
        sum += int(nums.group(1)) * int(nums.group(2))
    return sum

def part_two(input: str):

if __name__ == '__main__':
    main()