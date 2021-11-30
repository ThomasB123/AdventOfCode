infile = open('13input.txt','r')
for line in infile:
    buses = line[:-1]
buses = buses.split(',')
for i in range(len(buses)):
    if buses[i] != 'x':
        buses[i] = int(buses[i])

def productSoFar(x):
    product = 1
    for j in range(x):
        if buses[j] != 'x':
            product *= buses[j]
    return product

time = 1
for i in range(len(buses)):
    if buses[i] != 'x':
        newTime = time
        while (newTime+i)%buses[i] != 0:
            newTime += productSoFar(i)
        time = newTime

print(time)