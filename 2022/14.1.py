infile = open('14input.txt','r')
width = 1000
height = 200
cave = [['.' for i in range(width)] for j in range(height)]
for line in infile:
    coords = line[:-1].split(' -> ')
    for i in range(len(coords)-1):
        cur = coords[i].split(',')
        nex = coords[i+1].split(',')
        for j in range(int(cur[0]),int(nex[0])+1):
            for k in range(int(cur[1]),int(nex[1])+1):
                cave[k][j] = '#'
            for k in range(int(cur[1]),int(nex[1])-1,-1):
                cave[k][j] = '#'
        for j in range(int(cur[0]),int(nex[0])-1,-1):
            for k in range(int(cur[1]),int(nex[1])+1):
                cave[k][j] = '#'
            for k in range(int(cur[1]),int(nex[1])-1,-1):
                cave[k][j] = '#'
count = 0
while True:
    rest = False
    p = (0,500)
    while not rest:
        if p[0] == height-1:
            print(count)
            exit()
        elif cave[p[0]+1][p[1]] == '.':
            p = (p[0]+1,p[1])
        elif cave[p[0]+1][p[1]-1] == '.':
            p = (p[0]+1,p[1]-1)
        elif cave[p[0]+1][p[1]+1] == '.':
            p = (p[0]+1,p[1]+1)
        else:
            rest = True
            cave[p[0]][p[1]] = 'o'
    count += 1
