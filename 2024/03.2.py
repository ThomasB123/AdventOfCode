import re

infile = open('03input.txt')

filtered_input = []
for line in infile:
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)", line):
        filtered_input.append(line[match.start():match.end()])

total = 0
enabled = True
for x in filtered_input:
    if x == "do()":
        enabled = True
    elif x == "don't()":
        enabled = False
    elif enabled:
        for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", x):
            total += int(match[0]) * int(match[1])
print(total)
