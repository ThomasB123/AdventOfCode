infile = open('06input.txt','r')

group = {}
for x in 'abcdefghijklmnopqrstuvwxyz':
    group[x] = None
count = 0
for line in infile:
    if line == '\n':
        group = {}
        for x in 'abcdefghijklmnopqrstuvwxyz':
            group[x] = None
    else:
        for char in line[:-1]:
            if group[char] == None:
                count += 1
                group[char] = True
print(count)