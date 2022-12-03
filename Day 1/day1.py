import os

# read in the file, each sum = array index
sum_list = []
sum = 0
highest_value = 0
print(os.getcwd())
input_file = open("input_day1.txt", "r")
for line in input_file:
   if line != '\n':
      sum = sum + int(line)
   else:
      sum_list.append(sum)
      # if sum > highest_value:
      #    highest_value = sum
      sum = 0
# print(highest_value)
sum_list.sort(reverse=True)
high3 = sum_list[0] + sum_list[1] + sum_list[2]
print(sum_list[0])
print(high3)