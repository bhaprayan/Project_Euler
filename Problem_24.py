import itertools
digits = [0,1,2,3,4,5,6,7,8,9]
permute_list = list(itertools.permutations(digits))
b = ""
lexicographic = []
for i in permute_list:
    for a in i:    
        b += str(a)
    lexicographic.append(int(b))
    b = ""    
lexicographic.sort()
print lexicographic[999999]
