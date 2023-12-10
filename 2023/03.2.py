infile = open('03input.txt','r')

schematic = []
for line in infile:
    schematic.append([])
    for char in line[:-1]:
        schematic[-1].append(char)

partNumbers = []
number = False
for i in range(len(schematic)):
    for j in range(len(schematic[i])):
        if schematic[i][j].isdigit():
            if not number:
                partNumbers.append([])
            number = True
            partNumbers[-1].append([i,j])
        else:
            number = False

def getNumber(array):
    value = 0
    for i in range(len(array)):
        value = value * 10 + int(schematic[array[i][0]][array[i][1]])
    return value

def isGear(i,j):
    surrounding = []
    for a in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
        for b in partNumbers:
            if a in b and b not in surrounding:
                surrounding.append(b)
    if len(surrounding) == 2:
        return getNumber(surrounding[0]) * getNumber(surrounding[1])
    return 0

out = 0
for i in range(len(schematic)):
    for j in range(len(schematic[i])):
        if schematic[i][j] == '*':
            out += isGear(i,j)
print(out)
