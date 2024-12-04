infile = open('02input.txt')

total = 0
for line in infile:
    report = [int(x) for x in line.split(' ')]
    report_sorted = sorted(report)
    if report_sorted == report or sorted(report, reverse=True) == report:
        safe = True
        for i in range(len(report) - 1):
            if not (1 <= report_sorted[i+1] - report_sorted[i] <= 3):
                safe = False
        total += safe
print(total)
