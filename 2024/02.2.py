infile = open('02input.txt')

def is_safe(report):
    if ascending:
        for i in range(len(report) - 1):
            if not (1 <= report[i+1] - report[i] <= 3):
                return False
    else: 
        for i in range(len(report) - 1):
            if not (1 <= report[i] - report[i+1] <= 3):
                return False
    return True

total = 0
for line in infile:
    report = [int(x) for x in line.split(' ')]
    ascending = report[0] < report[-1]
    safe = is_safe(report)
    if not safe:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                safe = True
    total += safe
print(total)
