# a = 1 = x
# b = 2 = y
# c = 3 = z
# win = 6
# draw = 3
# lose = 0
# AX = 4
# AY = 8
# AZ = 9
# BX = 1
# BY = 5
# BZ= 9
# CX = 1
# CY = 2
# CZ = 6

sum = 0
input_file = open("input_day2.txt", "r")
for line in input_file:
    if "A" in line:
        if "X" in line:
            sum = sum + 4
        elif "Y" in line:
            sum = sum + 8
        elif "Z" in line:
            sum = sum + 9
    elif "B" in line:
        if "X" in line:
            sum = sum + 1
        elif "Y" in line:
            sum = sum + 5
        elif "Z" in line:
            sum = sum + 9
    elif "C" in line:
        if "X" in line:
            sum = sum + 1
        elif "Y" in line:
            sum = sum + 2
        elif "Z" in line:
            sum = sum + 6
print(sum)
