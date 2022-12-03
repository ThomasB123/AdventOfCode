infile = open('03input.txt','r')
out = 0
bags = []
count = 0
for line in infile:
    if count == 0:
        bags.append([])
    bags[-1].append(line[:-1])
    count = (count + 1) % 3

for i in bags:
    shared = ord(set(i[0]).intersection(i[1]).intersection(i[2]).pop())
    if shared < 91:
        out += shared - 38
    else:
        out += shared - 96
print(out)
