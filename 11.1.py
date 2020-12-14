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
    out = []
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (x != i or y != j) and 0 <= x < width and 0 <= y < height:
                out.append(seating[y][x])
    return out

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
                if '#' in neighbours:
                    newSeat = 'L'
                else:
                    newSeat = '#'
            elif current == '#':
                if neighbours.count('#') >= 4:
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