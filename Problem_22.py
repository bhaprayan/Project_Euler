file = open("/home/shubhankar/Documents/p022_names.txt")
names_list = []
for line in file:
    temp = line.split('"')  
    temp = sorted([i for i in temp if i!= ',' and i!= ''], key=str.lower)
name_scores = []
for i in temp:
    name_score = 0  
    for j in i:
        name_score += ord(j) - 64
    name_scores.append(name_score*(temp.index(i)+1))
print sum(name_scores)
