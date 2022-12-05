infile = open('05input.txt','r')
stacks = []
out = ''
for line in infile:
    stack = 0
    if not any(x.isdigit() for x in line):
        if (len(line)) // 4 != len(stacks):
            for i in range(len(line) // 4): stacks.append([])
        for i in range(len(line)):
            if (i-1) % 4 == 0:
                if line[i] != ' ':
                    stacks[stack].append(line[i])
                stack += 1
    if line[0] == 'm':
        commands = [eval(i) for i in [line.split()[j] for j in [1,3,5]]]
        for i in range(commands[0]):
            stacks[int(commands[2])-1].insert(0,stacks[int(commands[1])-1].pop(0))
for i in stacks:
    out += i[0]
print(out)
