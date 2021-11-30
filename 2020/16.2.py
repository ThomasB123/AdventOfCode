infile = open('16input.txt','r')
readIn = []
endOfRanges = False
rangeLength = 0
for line in infile:
    if line == '\n':
        endOfRanges = True
    rangeLength += not endOfRanges
    readIn.append(line[:-1])

ranges = []
overallRanges = {}
fields = {}
fieldNumber = {}
for i in range(rangeLength):
    fieldName = readIn[i].split(':')[0]
    fields[fieldName] = [x for x in range(rangeLength)]
    fieldNumber[i] = fieldName
    ranges.append([])
    line = readIn[i].split()
    firstRange = line[-3].split('-')
    for j in range(int(firstRange[0]),int(firstRange[1])+1):
        ranges[-1].append(j)
        overallRanges[j] = None
    secondRange = line[-1].split('-')
    for j in range(int(secondRange[0]),int(secondRange[1])+1):
        ranges[-1].append(j)
        overallRanges[j] = None

myTicket = readIn[rangeLength+2].split(',')

validTickets = []

for i in range(rangeLength+5,len(readIn)):
    numbers = readIn[i].split(',')
    valid = True
    for j in range(len(numbers)):
        if int(numbers[j]) not in overallRanges:
            valid = False
    if valid:
        for j in range(len(numbers)): # j is value to remove
            for k in range(len(ranges)):
                if (int(numbers[j]) not in ranges[k]) and (j in fields[fieldNumber[k]]):
                    fields[fieldNumber[k]].remove(j)

remove = []
done = False
while not done:
    done = True
    for x in fields:
        if len(fields[x]) == 1:
            if fields[x][0] not in remove:
                remove.append(fields[x][0])
        elif len(fields[x]) > 1:
            done = False
            for y in remove:
                if y in fields[x]:
                    fields[x].remove(y)

out = 1
for x in fields:
    if x.split()[0] == 'departure':
        out *= int(myTicket[fields[x][0]])
print(out)