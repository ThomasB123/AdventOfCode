infile = open('01input.txt','r')
count, number = 0, 50
for line in infile:
    rotation = int(line[1:-1])
    if line[0] == 'R':
        for i in range(rotation):
            number += 1
            count += (number % 100 == 0)
    else:
        for i in range(rotation):
            number -= 1
            count += (number % 100 == 0)
print(count)
