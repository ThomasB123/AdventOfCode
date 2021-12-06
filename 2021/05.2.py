inFile = open('05input.txt','r')
lines = []
maxi = []
for line in inFile:
    xy = line[:-1].split(' -> ')
    x = xy[0].split(',')
    y = xy[1].split(',')
    lines.append([[int(x[0]),int(x[1])],[int(y[0]),int(y[1])]])
    maxi.append(int(x[0]))
    maxi.append(int(x[1]))
    maxi.append(int(y[0]))
    maxi.append(int(y[1]))

maximum = max(maxi) + 1
field = []
for i in range(maximum):
    field.append([])
    for j in range(maximum):
        field[i].append(0)

for coord in lines:
    if coord[0][1] == coord[1][1]:
        small = min(coord[0][0],coord[1][0])
        big = max(coord[0][0],coord[1][0])
        for hole in range(small,big+1):
            field[coord[0][1]][hole] += 1
    elif coord[0][0] == coord[1][0]:
        small = min(coord[0][1],coord[1][1])
        big = max(coord[0][1],coord[1][1])
        for hole in range(small,big+1):
            field[hole][coord[0][0]] += 1
    elif coord[0][0] < coord[1][0]:
        gap = coord[1][0] - coord[0][0] + 1
        if coord[0][1] < coord[1][1]:
            for i in range(gap):
                field[coord[0][1]+i][coord[0][0]+i] += 1
        else:
            for i in range(gap):
                field[coord[0][1]-i][coord[0][0]+i] += 1
    else:
        gap = coord[0][0] - coord[1][0] + 1
        if coord[0][1] < coord[1][1]:
            for i in range(gap):
                field[coord[0][1]+i][coord[0][0]-i] += 1
        else:
            for i in range(gap):
                field[coord[0][1]-i][coord[0][0]-i] += 1
count = 0
for f in field:
    count += len(f)-f.count(1)-f.count(0)
print(count)