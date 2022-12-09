infile = open('09input.txt','r')
visited = {}
p = [[0,0] for i in range(10)]
for line in infile:
    [command,moves] = line.split()
    for i in range(int(moves)):
        if command == 'R':
            p[0][0] += 1
        elif command == 'L':
            p[0][0] -= 1
        elif command == 'U':
            p[0][1] += 1
        elif command == 'D':
            p[0][1] -= 1
        for j in range(9):
            if p[j][0]-p[j+1][0] >= 2:
                p[j+1][0] += 1
                if p[j][1]-p[j+1][1] >= 1:
                    p[j+1][1] += 1
                elif p[j+1][1]-p[j][1] >= 1:
                    p[j+1][1] -= 1
            elif p[j+1][0]-p[j][0] >= 2:
                p[j+1][0] -= 1
                if p[j][1]-p[j+1][1] >= 1:
                    p[j+1][1] += 1
                elif p[j+1][1]-p[j][1] >= 1:
                    p[j+1][1] -= 1
            elif p[j][1]-p[j+1][1] >= 2:
                p[j+1][1] += 1
                if p[j][0]-p[j+1][0] >= 1:
                    p[j+1][0] += 1
                elif p[j+1][0]-p[j][0] >= 1:
                    p[j+1][0] -= 1
            elif p[j+1][1]-p[j][1] >= 2:
                p[j+1][1] -= 1
                if p[j][0]-p[j+1][0] >= 1:
                    p[j+1][0] += 1
                elif p[j+1][0]-p[j][0] >= 1:
                    p[j+1][0] -= 1
            visited['.'.join([str(p[-1][0]),str(p[-1][1])])] = None
print(len(visited))
