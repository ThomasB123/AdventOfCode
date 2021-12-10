inFile = open('06input.txt','r')
fish = []
for f in inFile.readline()[:-1].split(','):
    fish.append(int(f))

numbers = [0,0,0,0,0,0,0,0,0]
for f in fish:
    numbers[f] += 1

for i in range(256):
    newNumbers = [0,0,0,0,0,0,0,0,0]
    for j in range(9):
        if j > 0:
            newNumbers[j-1] += numbers[j]
        else:
            newNumbers[6] += numbers[j]
            newNumbers[8] += numbers[j]
    numbers = newNumbers
print(sum(numbers))
