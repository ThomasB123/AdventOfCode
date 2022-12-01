infile = open('01input.txt','r')
calories = [0]
for line in infile:
    if len(line) > 1:
        calories[-1] += int(line[:-1])
    else:
        calories.append(0)
print(sum(sorted(calories)[-3:]))
