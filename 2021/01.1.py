infile = open('01input.txt','r')
depths = []
for line in infile:
    depths.append(int(line[:-1]))

count = 0
previous = depths[0]
for depth in depths[1:]:
    if depth > previous:
        count += 1
    previous = depth
print(count)