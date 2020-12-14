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
            inside.append([words[x+4],' '.join(words[x+5:x+7])])
        bags[bagName] = inside

# breadth first search
count = 0
queue = [['1','shiny gold']]
while queue != []:
    currentBag = queue.pop(0)
    mult = int(currentBag[0])
    nextBags = bags[currentBag[1]]
    count += mult
    if nextBags != None:
        for x in nextBags:
            queue.append([int(x[0])*mult,x[1]])
print(count-1)
