infile = open('03input.txt','r')
index = 0
count = 0
for line in infile:
    count += line[index] == '#'
    index = (index + 3) % (len(line)-1)
print(count)