infile = open('03input.txt')

schematic = []
for line in infile:
    schematic.append([])
    for char in line[:-1]:
        schematic[-1].append(char)

def isPartNumber(i,j):
    partNumber = False
    for a in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
        if 0 <= a[0] < len(schematic) and 0 <= a[1] < len(schematic[0]):
            if not schematic[a[0]][a[1]].isdigit() and schematic[a[0]][a[1]] != '.':
                partNumber = True
    return partNumber

out = 0
partNumber = False
for i in range(len(schematic)):
    if partNumber:
        out += number
    number = 0
    partNumber = False
    for j in range(len(schematic[i])):
        if schematic[i][j].isdigit():
            number = number * 10 + int(schematic[i][j])
            if isPartNumber(i,j):
                partNumber = True
        else:
            if partNumber:
                out += number
            partNumber = False
            number = 0
print(out)
