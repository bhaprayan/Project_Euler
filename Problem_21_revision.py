def Divisor_List(n,m):
    for i in range(n):
        if n % i == 0:
            divisor_list_0.append(i)
    for i in range(m):
        if m % i == 0:
            divisor_list_1.append(i)
    if sum(divisor_list_0) == m and sum(divisor_list_1) == n:
        return True
    else:
        return False
Amicable = []

for i in range(10000):
    for j in range(10000):
        if Divisor_List(i,j) == True:
            Amicable.append(i)
            Amicable.append(j)

print sum(Amicable)
