infile = open('03input.txt','r')
numbers = []
for line in infile:
    numbers.append(line[:-1])

sums = []
for i in range(len(numbers[0])):
    sums.append(0)
    for j in range(len(numbers)):
        sums[i] += int(numbers[j][i])
    if sums[i] <= len(numbers)//2:
        sums[i] = 0
    else:
        sums[i] = 1

mult = 1
gamma = 0
for i in range(len(sums)-1,-1,-1):
    gamma += sums[i] * mult
    mult *= 2

epsilon = 2**len(numbers[0]) - 1 - gamma
print(gamma * epsilon)