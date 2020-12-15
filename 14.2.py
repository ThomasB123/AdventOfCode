infile = open('14input.txt','r')
mask = 'X'
mem = {}
for line in infile:
    if line[1] == 'a':
        mask = line.split()[-1]
    else:
        bracket = line.index(']')
        integer = int(line[4:bracket])
        binary = str(bin(integer))[2:]
        while len(binary) < 36:
            binary = '0' + binary
        newBinary = ['']
        for i in range(len(binary)-1,-1,-1):
            maskBit = mask[i]
            if maskBit == 'X':
                length = len(newBinary)
                for j in range(length):
                    newBinary.append('1' + newBinary[j])
                    newBinary[j] = '0' + newBinary[j]
            elif maskBit == '0':
                for j in range(len(newBinary)):
                    newBinary[j] = binary[i] + newBinary[j]
            elif maskBit == '1':
                for j in range(len(newBinary)):
                    newBinary[j] = '1' + newBinary[j]
        for x in newBinary:
            integer = int(x,2)
            mem[integer] = int(line.split()[-1])
total = 0
for i in mem:
    total += mem[i]
print(total)