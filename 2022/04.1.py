infile = open('04input.txt','r')
count = 0
for line in infile:
    halves = line.split((','))
    first = [eval(i) for i in (halves[0].split('-'))]
    second = [eval(i) for i in (halves[1].split('-'))]
    if first[0] <= second[0] and first[1] >= second[1] or first[0] >= second[0] and first[1] <= second[1]:
        count += 1
print(count)
