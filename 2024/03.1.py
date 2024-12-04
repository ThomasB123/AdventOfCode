import re

infile = open('03input.txt')

total = 0
for line in infile:
    for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
        total += int(match[0]) * int(match[1])
print(total)
