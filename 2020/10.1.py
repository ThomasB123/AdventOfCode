infile = open('10input.txt','r')
adapters = []
for line in infile:
    adapters.append(int(line))
adapters.sort()

one = 0
three = 1
last = 0
for x in range(len(adapters)):
    if adapters[x] - last == 1:
        one += 1
    else:
        three += 1
    last = adapters[x]
print(one*three)