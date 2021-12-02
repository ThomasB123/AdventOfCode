infile = open('02input.txt','r')
forward = 0
depth = 0
for line in infile:
    instruction = line[:-1].split()[0]
    magnitude = int(line[:-1].split()[1])
    if instruction == 'forward':
        forward += magnitude
    elif instruction == 'down':
        depth += magnitude
    elif instruction == 'up':
        depth -= magnitude
print(forward*depth)