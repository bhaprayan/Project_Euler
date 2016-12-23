import math
summation = 0
digit_list = []
for i in xrange(3, 9*math.factorial(9)):
    a = [int(j) for j in str(i)]
    for j in a:
        summation += math.factorial(j) 
    if summation == i:
        digit_list.append(summation)
    else:
        summation = 0

print sum(digit_list)
