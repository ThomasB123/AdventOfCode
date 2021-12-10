inFile = open('07input.txt','r')
crabs = []
for c in inFile.readline()[:-1].split(','):
    crabs.append(int(c))

fuels = []
for i in range(max(crabs)):
    fuel = 0
    for j in crabs:
        fuel += abs(j-i)
    fuels.append(fuel)

print(min(fuels))
