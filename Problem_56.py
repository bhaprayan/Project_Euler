number_list = []
for i in range(100):
    for j in range(100):
        number = i ** j
        number_list.append(sum([int(k) for k in str(number)]))
number_list.sort()
print number_list.pop()
