import re
list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

real_list_1 = []
real_list_2 = []
with(open("message.txt",'r')) as message:
    string = message.readline()
    while string != None and string != "":
        print(string)
        numbers = re.match("([0-9]+)   ([0-9]+)",string)
        if numbers != None:
            real_list_1.append(int(numbers.group(1)))
            real_list_2.append(int(numbers.group(2)))
        string = message.readline()
      

def part_one(list1:list,list2:list) -> int:
    if len(list1) != len(list2):
        raise AttributeError("Cannot deal with differnet sized lists")
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    difference = 0
    for _ in range(len(list1)):
        temp_dif = abs(list1.pop() - list2.pop())
        difference += temp_dif
    
    return difference
        
def part_two(list1,list2) -> int:
    ref_dict = {} #{key = each of the unique numbers in list2, value = times it appears in the list}
    for number in list2:
        if number in ref_dict.keys():
            ref_dict[number] += 1 #not sure if this is right
        else:
            ref_dict[number] = 1

    return_val = 0
    for number in list1:
        if number in ref_dict.keys():
            temp_sim = number * ref_dict[number]
            return_val += temp_sim
    return return_val


#print(part_one(real_list_1,real_list_2))
#print(part_two(real_list_1,real_list_2))







# pair smallest list 1 with list 2
# subtract
# add up difference 
# return val



#sort lists
#pop 0th off both, and subtract