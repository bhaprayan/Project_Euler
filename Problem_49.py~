import Sieve_Eratosthenes as se 
import itertools , math
prime_array = se.Sieve()
prime_array = [i for i in prime_array if len(str(i)) > 3]
counter = 0
prime_list = []
for j in prime_array:
    permutations = [int(i) for i in map("".join , itertools.permutations(str(j)))]
    permutations = set(permutations) 
    for i in permutations:
        if i in prime_array:
            prime_list.append(i)
        if len(prime_list) >= 3:
            prime_list.sort()  
            for i in reversed(range(1,len(prime_list))):
                diff = prime_list[i] - prime_list[i-1]
                diff1 = prime_list[i-1] - prime_list[i-2]
                if diff == diff1: 
                    print prime_list 
    counter = 0
    prime_list = []
