sum = ""
d = 1
for i in range (1,1000000):sum += str(i)
for i in range(0,6):d *= int(sum[(10**i)-1])
print d 
