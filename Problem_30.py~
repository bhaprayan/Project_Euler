summation = 0
digit_list = []
for i in range(2, 6*(9**5)):
    a = [int(j) for j in str(i)]
    for j in a:
        summation += j**5
    if summation == i:
        digit_list.append(summation)
    else:
        summation = 0
        a = []    
print sum(digit_list)
