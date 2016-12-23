import Sieve_Eratosthenes as se
import itertools
def Circular_Permute(i):
    temp = "" 
    circular_permute = [] 
    b = [j for j in str(i)]
    for j in range(len(b)):
        b.insert(0, b.pop())
        for l in b:
            temp += l
        circular_permute.append(int(temp))
        temp = "" 
    return circular_permute
prime = se.Sieve(1000000)
counter = 0
circular_prime = [] 
for i in prime:
    permute = Circular_Permute(i)
    if i in circular_prime:
        continue
    else:
        for j in permute:
            if j in prime:
                counter += 1
            if counter == len(permute):
                circular_prime.append(i) 
        counter = 0 
print len(circular_prime)
