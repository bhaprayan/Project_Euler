import math

def prime_number_check(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:     
            return False
    return True 

def First_Number(n):
     return (3 * 2**(n-1)) - 1
def Second_Number(n):
   return (3 * 2**(n)) - 1
def Third_Number(n):
    return (9 *(2**(2*n - 1))) - 1

def First_Ami(n):
    return  (2 ** n)* First_Number(n)* Second_Number(n)
 
def Second_Ami(n):
    return (2 ** n) * Third_Number(n) 

sum = 0

i = 2 
while (First_Ami(i) < 100000):
    if prime_number_check(First_Number(i)) and prime_number_check(Second_Number(i)):
        if prime_number_check(Third_Number(i)):
            print First_Ami(i)
    i += 1

i = 2
while (Second_Ami(i) < 100000):
    if prime_number_check(First_Number(i)) and prime_number_check(Second_Number(i)):
        if prime_number_check(Third_Number(i)):
            print Second_Ami(i)
    i += 1

print sum
