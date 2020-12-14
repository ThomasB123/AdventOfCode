infile = open('11input.txt','r')
seating = []
for line in infile:
    add = []
    for seat in line[:-1]:
        add.append(seat)
    seating.append(add)
width = len(seating[0])
height = len(seating)

def getNeighbours(i,j):
    if seating[j][i] == '.':
        return 0
    count = 0
    if i > 0:
        x,y = i-1,j
        while x >= 1 and seating[y][x] == '.':
            x -= 1
        count += seating[y][x] == '#'
    if i < width-1:
        x,y = i+1,j
        while x < width-1 and seating[y][x] == '.':
            x += 1
        count += seating[y][x] == '#'
    if j > 0:
        x,y = i,j-1 
        while y >= 1 and seating[y][x] == '.':
            y -= 1
        count += seating[y][x] == '#'
    if j < height-1:
        x,y = i,j+1
        while y < height-1 and seating[y][x] == '.':
            y += 1
        count += seating[y][x] == '#'
    if i > 0 and j > 0:
        x,y = i-1,j-1
        while x >= 1 and y >= 1 and seating[y][x] == '.':
            x -= 1
            y -= 1
        count += seating[y][x] == '#'
    if i > 0 and j < height-1:
        x,y = i-1,j+1
        while x >= 1 and y < height-1 and seating[y][x] == '.':
            x -= 1
            y += 1
        count += seating[y][x] == '#'
    if i < width-1 and j > 0:
        x,y = i+1,j-1
        while x < width-1 and y >= 1 and seating[y][x] == '.':
            x += 1
            y -= 1
        count += seating[y][x] == '#'
    if i < width-1 and j < height-1:
        x,y = i+1,j+1
        while x < width-1 and y < height-1 and seating[y][x] == '.':
            x += 1
            y += 1
        count += seating[y][x] == '#'
    return count

def iterate():
    out = []
    for i in range(height):
        out.append([])
        for j in range(width):
            current = seating[i][j]
            neighbours = getNeighbours(j,i)
            if current == '.':
                newSeat = '.'
            elif current == 'L':
                if neighbours >= 1:
                    newSeat = 'L'
                else:
                    newSeat = '#'
            elif current == '#':
                if neighbours >= 5:
                    newSeat = 'L'
                else:
                    newSeat = '#'
            out[-1].append(newSeat)
    return out

oldSeating = []
while oldSeating != seating:
    oldSeating = seating
    seating = iterate()
count = 0
for x in seating:
    count += x.count('#')
print(count)