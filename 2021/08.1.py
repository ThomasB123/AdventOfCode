inFile = open('08input.txt','r')
outputs = []
for line in inFile:
    outputs.append(line[:-1].split(' | ')[-1])

numbers = []
for i in outputs:
    for j in i.split():
        numbers.append(j)

count = 0
for i in numbers:
    if len(i) in [2,4,3,7]:
        count += 1
print(count)
