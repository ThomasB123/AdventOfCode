infile = open('09input.txt','r')
buffer = 25
numbers = []
allNumbers = []
for line in infile:
    if len(numbers) == buffer:
        target = int(line)
        found = False
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    found = True
        if not found:
            invalid = target
        numbers.pop(0)
    numbers.append(int(line))
    allNumbers.append(int(line))

found = False
x = -1
while not found:
    x += 1
    y = x + 1
    total = allNumbers[x]+allNumbers[y]
    while total < invalid:
        y += 1
        total += allNumbers[y]
        if total == invalid:
            found = True
print(min(allNumbers[x:y+1])+max(allNumbers[x:y+1]))