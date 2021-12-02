infile = open('01input.txt','r')
depths = []
for line in infile:
    depths.append(int(line[:-1]))

count = 0
previous = sum([depths[0],depths[1],depths[2]])
for i in range(2,len(depths)-1):
    window = sum([depths[i-1],depths[i],depths[i+1]])
    if window > previous:
        count += 1
    previous = window
print(count)