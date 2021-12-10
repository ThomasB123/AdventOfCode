inFile = open('07input.txt','r')
crabs = []
for c in inFile.readline()[:-1].split(','):
    crabs.append(int(c))

triangular = [0]
fuels = []
for i in range(max(crabs)):
    fuel = 0
    for j in crabs:
        diff = abs(j-i)
        while diff >= len(triangular):
            triangular.append(triangular[-1] + len(triangular))
        fuel += triangular[diff]
    fuels.append(fuel)

print(min(fuels))
