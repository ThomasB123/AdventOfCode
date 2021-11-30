infile = open('16input.txt','r')
readIn = []
endOfRanges = False
rangeLength = 0
for line in infile:
    if line == '\n':
        endOfRanges = True
    rangeLength += not endOfRanges
    readIn.append(line[:-1])

ranges = {}
for i in range(rangeLength):
    line = readIn[i].split()
    firstRange = line[-3].split('-')
    for j in range(int(firstRange[0]),int(firstRange[1])+1):
        ranges[j] = None
    secondRange = line[-1].split('-')
    for j in range(int(secondRange[0]),int(secondRange[1])+1):
        ranges[j] = None

count = 0
for i in range(rangeLength+5,len(readIn)):
    numbers = readIn[i].split(',')
    for j in range(len(numbers)):
        if int(numbers[j]) not in ranges:
            count += int(numbers[j])
print(count)