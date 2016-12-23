def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1,int(n**0.5) + 1) if n % i == 0)))

Amicable = []

for i in range(4,9999):
    for j in range(i+1,10000):
        if sum(factors(i)) == sum(factors(j)):
            Amicable.append(i)
            Amicable.append(j)

print sum(Amicable)

