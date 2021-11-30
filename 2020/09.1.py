infile = open('09input.txt','r')
buffer = 25
numbers = []
for line in infile:
    if len(numbers) == buffer:
        target = int(line)
        found = False
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    found = True
        if not found:
            break
        numbers.pop(0)
    numbers.append(int(line))
print(target)