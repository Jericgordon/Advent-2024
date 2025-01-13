import re

def get_inputs(file_name:str):
    updates = []
    rulebook = {}
    with open(file_name,'r') as file:
        line = file.readline()
        while line != "":
            if line == "\n":
                line = file.readline()
                continue
            pattern = "([0-9]+)[|]([0-9]+)"
            inst = re.match(pattern,line)
            if inst == None and len(line) > 1:
                updates.append(re.findall("[0-9]+",line))
            elif  int(inst.group(1)) in rulebook:
                rulebook[int(inst.group(1))].append(int(inst.group(2)))
            else:
                rulebook[int(inst.group(1))] = [int(inst.group(2))]
            line = file.readline()
    return rulebook,updates

def part_one(file_name:str) -> int:
    rulebook,updates = get_inputs(file_name)
    sum = 0
    for update in updates:
        if rule_checker(rulebook,update):
            sum += int(update[len(update) // 2])
    return sum

def rule_checker(rulebook:dict, update:list) -> bool:
    seen = {} #the page_numbers we've seen before in this update; 1 is seen
    for page in update:
        page = int(page)
        seen[page] = 1 #mark the page as seen before
        if page not in rulebook:
            continue
        rules = rulebook[page]
        for rule in rules:
            if rule in seen:
                return False
    return True

def part_two(file_name:str) -> int:
    rulebook,updates = get_inputs(file_name)
    sum = 0
    for update in updates:
        if not rule_checker(rulebook,update):
            fixed_list = fix_list(update,rulebook)
            sum += int(fixed_list[len(fixed_list) // 2])
    return sum
    

def fix_list(update:list,rulebook:dict) -> list:
    final_list = []
    seen = {}
    for index in range(len(update)):
        single_update = int(update[index])
        if single_update not in seen:
            seen[single_update] = index

        if single_update not in rulebook:
            final_list.append(single_update)
            continue
        rules = rulebook[single_update]
        insert = False
        index_to_insert = 1000000
        for rule in rules:
            if rule in seen:
                index_of_rule_break = seen[rule]
                if index_of_rule_break < index_to_insert:
                    index_to_insert = index_of_rule_break
                insert = True
        if insert:
            final_list.insert(index_to_insert,single_update)
            for new_index in range(index_to_insert,len(final_list)):
                seen[final_list[new_index]] = new_index
                
        else:
            final_list.append(single_update)
    return final_list



if __name__ == '__main__':
    print("part 1:",part_one("day_5.txt"))
    print("part 2:",part_two("day_5.txt"))
