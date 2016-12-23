import Sieve_Eratosthenes as se
s = [i for i in range(1,9)]
a = se.Sieve(1000000)
for i in a:
    digits = [int(j) for j in str(i)]
    if digits.sort() == s:
        pandigital.append(i) 
pandigital.sort()
print pandigital.pop()
