db_palin = []
for i in xrange(1000000):
    b = bin(i)[2:]
    if str(i) == str(i)[::-1] and b == b[::-1]:
        db_palin.append(i)
print sum(db_palin)
