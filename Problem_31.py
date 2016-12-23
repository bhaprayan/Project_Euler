import Sieve_Eratosthenes as se
pandigital = []
s = [i for i in range(1,10)]
a = se.Sieve(10000000)
for i in a:
    digits = [int(j) for j in str(i)]
    if digits.sort() == s:
        pandigital.append(i)
    else:
        digits = []
pandigital.sort()
print pandigital
