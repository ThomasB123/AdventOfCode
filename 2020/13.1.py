infile = open('13input.txt','r')
inData = []
for line in infile:
    inData.append(line[:-1])
earliest, buses = inData
earliest = int(earliest)
buses = buses.split(',')

smallestWait = earliest
smallestBus = 0
for i in buses:
    if i != 'x':
        i = int(i)
        wait = i- (earliest % i)
        if wait < smallestWait:
            smallestWait = wait
            smallestBus = i
print(smallestWait*smallestBus)