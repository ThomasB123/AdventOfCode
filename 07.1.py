infile = open('07input.txt','r')

bags = {}
contain = []
for line in infile:
    words = line.split()
    bagName = ' '.join(words[:2])
    if len(words) == 7:
        bags[bagName] = None
    else:
        inside = []
        for x in range(00,(len(words)-4),4):
            inside.append(' '.join(words[x+5:x+7]))
        bags[bagName] = inside

while True:
    count = 0
    for x in bags:
        if bags[x] != None:
            if 'shiny gold' in bags[x] and x not in contain:
                count += 1
                contain.append(x)
            for i in bags[x]:
                if i in contain and x not in contain:
                    count += 1
                    contain.append(x)
    if count == 0:
        break
print(len(contain))
