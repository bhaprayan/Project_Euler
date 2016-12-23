for i in xrange(1000):
    for j in xrange(1000):
        for n in range(1000):
            formula = n**2 + i*n + j 
            if formula in primes:
                counter+= 1
            else:
                if counter > max_counter
