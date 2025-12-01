infile = open('01input.txt','r')
count, number = 0, 50
for line in infile:
    rotation = int(line[1:-1])
    if line[0] == 'R': number += rotation
    else: number -= rotation
    number %= 100
    count += number == 0
print(count)
