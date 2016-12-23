Month_table_normal = [0,3,3,6,1,4,6,2,5,0,3,5]
Month_table_leap = [6,2,3,6,1,4,6,2,5,0,3,5]

Sunday_count = 0

for y in range(1901,2000):
    if y % 4 != 0: 
        for m in Month_table_normal:
            year = [c for c in str(y)] 
            year_now = int(year[2] + year[3])
            x = (1+ m + year_now + year_now/4 + 0 ) % 7
            if x == 0:
                Sunday_count += 1
    else: 
        for m in Month_table_leap:
            year = [c for c in str(y)] 
            year_now = int(year[2] + year[3])
            x = (1+ m + year_now + year_now/4 + 0 ) % 7
            if x == 0:
                Sunday_count += 1
y = 2000
if y % 4 != 0: 
    for m in Month_table_normal:
        year = [c for c in str(y)] 
        year_now = int(year[2] + year[3])
        x = (1+ m + year_now + year_now/4 + 6 ) % 7
        if x == 0:
            Sunday_count += 1
else: 
    for m in Month_table_leap:
        year = [c for c in str(y)] 
        year_now = int(year[2] + year[3])
        x = (1+ m + year_now + year_now/4 + 6 ) % 7
        if x == 0:
            Sunday_count += 1




print Sunday_count
