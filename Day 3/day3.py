import string

# use dict to get priority value
priority = {}
start = 1
for key in string.ascii_letters:
    priority[key] = start
    start = start + 1

# part 1
# read string
# sum = 0
# count = 1
# rucksacks = [0,0]
# input_file = open("input_day3.txt", "r")
# for line in input_file:
#     # remove \n
#     if "\n" in line:
#         line = line[0:len(line)-1]
#     # split in half
#     rucksacks[0] = line[:len(line)//2]
#     rucksacks[1] = line[len(line)//2:]
#     # print(len(line))
    
    
#     # find common item
#     char = "".join(set(rucksacks[0]).intersection(rucksacks[1]))
#     sum = sum + priority[char]
    
#     print(f'count = {count}' + "\t" + f'sum = {sum}' + "\t" + f'char = {char}' + "\t" + f'priority = {priority[char]}')
#     print(rucksacks[0]+ " " + rucksacks[1]+"\n\n")
#     count = count + 1
# print(sum)

# part 2
# read string
sum = 0
count = 1
rucksacks = [0,0,0]
input_file = open("input_day3.txt", "r")
for line in input_file:
    # remove \n
    if "\n" in line:
        line = line[0:len(line)-1]
    if count%3 != 0:
        rucksacks[count-1] = line
        count = count + 1
    else:
        rucksacks[count-1] = line
        # find common item
        char = "".join(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))
        sum = sum + priority[char]
        print(f'count = {count}' + "\t" + f'sum = {sum}' + "\t" + f'char = {char}' + "\t" + f'priority = {priority[char]}')
        print(rucksacks[0]+ " " + rucksacks[1]+"\n\n")
        count = 1
    
print(sum)