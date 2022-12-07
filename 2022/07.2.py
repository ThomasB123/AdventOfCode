infile = open('07input.txt','r')
sizes = {}
path = []
for line in infile:
    commands = line.split()
    if commands[0] == '$':
        if commands[1] == 'cd':
            if commands[2] == '..':
                path.pop()
            elif commands[2] != '/':
                path.append(commands[2]+'/')
            else:
                path.append(commands[2])
    elif commands[0] != 'dir':
        for i in range(len(path),0,-1):
            if ''.join(path[:i]) not in sizes:
                sizes[''.join(path[:i])] = 0
            sizes[''.join(path[:i])] += int(commands[0])
required = 30000000-(70000000-sizes['/'])
smallest = sizes['/']
for i in sizes:
    if required < sizes[i] < smallest:
        smallest = sizes[i]
print(smallest)
