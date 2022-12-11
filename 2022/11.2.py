infile = open('11input.txt','r')
monkey = 0
monkeys = {0:[]}
items = [[]]
for line in infile:
    if line == '\n':
        monkey += 1
        monkeys[monkey] = []
        items.append([])
    elif line[2] == 'S':
        for i in (line[:-1].split(':')[1]).split(','):
            items[monkey].append(int(i))
    elif line[2] == 'O':
        for i in (line[:-1].split('= ')[1].split()[1:]):
            monkeys[monkey].append(i)
    elif line[0] != 'M':
        monkeys[monkey].append(int(line.split()[-1]))

quotient = 1
for i in monkeys:
    quotient *= monkeys[i][2]

count = [0 for i in range(len(items))]
for i in range(10000):
    for j in range(len(items)):
        num = len(items[j])
        for k in range(num):
            items[j][0] %= quotient
            count[j] += 1
            if monkeys[j][0] == '+':
                if monkeys[j][1] == 'old':
                    items[j][0] *= 2
                else:
                    items[j][0] += int(monkeys[j][1])
            else:
                if monkeys[j][1] == 'old':
                    items[j][0] **= 2
                else:
                    items[j][0] *= int(monkeys[j][1])
            if items[j][0] % monkeys[j][2] == 0:
                items[monkeys[j][3]].append(items[j][0])
            else:
                items[monkeys[j][4]].append(items[j][0])
            items[j].pop(0)
count.sort()
print(count[-1]*count[-2])
