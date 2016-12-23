file = open("/home/shubhankar/Documents/Input_Numbers")
number_list = []
for line in file:
    number_list.append(int(line.rstrip()))
sum = 0
for i in range(len(number_list)):
    sum += number_list[i]
print sum
