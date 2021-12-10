inFile = open('06input.txt','r')
fish = []
for f in inFile.readline()[:-1].split(','):
    fish.append(int(f))

for i in range(80):
    newFish = []
    for f in fish:
        if f > 0:
            newFish.append(f-1)
        else:
            newFish.append(6)
            newFish.append(8)
    fish = newFish
print(len(fish))