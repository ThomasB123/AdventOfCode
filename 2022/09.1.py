infile = open('09input.txt','r')
visited = {}
h,t = [0,0],[0,0]
for line in infile:
    [command,moves] = line.split()
    for i in range(int(moves)):
        if command == 'R':
            h[0] += 1
        elif command == 'L':
            h[0] -= 1
        elif command == 'U':
            h[1] += 1
        elif command == 'D':
            h[1] -= 1
        if h[0]-t[0] == 2:
            t[0] += 1
            if h[1]-t[1] == 1:
                t[1] += 1
            elif t[1]-h[1] == 1:
                t[1] -= 1
        elif t[0]-h[0] == 2:
            t[0] -= 1
            if h[1]-t[1] == 1:
                t[1] += 1
            elif t[1]-h[1] == 1:
                t[1] -= 1
        elif h[1]-t[1] == 2:
            t[1] += 1
            if h[0]-t[0] == 1:
                t[0] += 1
            elif t[0]-h[0] == 1:
                t[0] -= 1
        elif t[1]-h[1] == 2:
            t[1] -= 1
            if h[0]-t[0] == 1:
                t[0] += 1
            elif t[0]-h[0] == 1:
                t[0] -= 1
        visited['.'.join([str(t[0]),str(t[1])])] = None
print(len(visited))
