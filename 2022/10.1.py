infile = open('10input.txt','r')
x = 1
cycle = 0
out = 0
for line in infile:
    cycle += 1
    if (cycle-20) % 40 == 0:
        out += cycle*x
    if line[0] == "a":
        cycle += 1
        if (cycle-20) % 40 == 0:
            out += cycle*x
        x += int(line.split()[1])
print(out)
