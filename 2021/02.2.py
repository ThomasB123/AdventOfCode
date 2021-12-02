infile = open('02input.txt','r')
forward = 0
depth = 0
aim = 0
for line in infile:
    instruction = line[:-1].split()[0]
    magnitude = int(line[:-1].split()[1])
    if instruction == 'forward':
        forward += magnitude
        depth += magnitude * aim
    elif instruction == 'down':
        aim += magnitude
    elif instruction == 'up':
        aim -= magnitude
print(forward*depth)