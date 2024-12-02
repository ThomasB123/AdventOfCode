infile = open('01input.txt')

left = []
right = []
for line in infile:
    numbers = line[:-1].split('   ')
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

total = 0
for i in left:
    total += i * right.count(i)
print(total)
