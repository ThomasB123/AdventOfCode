infile = open('01input.txt')

left = []
right = []
for line in infile:
    numbers = line[:-1].split('   ')
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total)
