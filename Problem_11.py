file = open("/home/shubhankar/Documents/Input_Grid")
current_line = []
for line in file:
    current_line.append(line.split())
Largest_Product = 0
for i in range(20):
    for j in range(16):
        Product = int(current_line[i][j]) * int(current_line[i][j+1]) * int(current_line[i][j+2])  * int(current_line[i][j+3])
        if Product > Largest_Product :  Largest_Product = Product 
        Product = int(current_line[j][i]) * int(current_line[j][i+1]) * int(current_line[j][i+2])  * int(current_line[j][i+3])
        if Product > Largest_Product :  Largest_Product = Product 
for i in range(16):
    for j in range(3,20):
        Product = int(current_line[i][j]) * int(current_line[i+1][j-1]) * int(current_line[i+2][j-2])  * int(current_line[i+3][j-3])
        if Product > Largest_Product :  Largest_Product = Product 
for i in range(16):
    for j in range(16):
        Product = int(current_line[i][j]) * int(current_line[i+1][j+1]) * int(current_line[i+2][j+2])  * int(current_line[i+3][j+3])  
        if Product > Largest_Product :  Largest_Product = Product 

print Largest_Product



