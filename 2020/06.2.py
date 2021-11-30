infile = open('06input.txt','r')

letters = 'abcdefghijklmnopqrstuvwxyz'
group = []
for x in letters:
    group.append(x)
count = 0
for line in infile:
    if line == '\n':
        count += len(group)
        group = []
        for x in letters:
            group.append(x)
    else:
        for letter in letters:
            if letter in group and letter not in line[:-1]:
                group.remove(letter)
print(count)