infile = open('14input.txt','r')
mask = 'X'
mem = {}
for line in infile:
    if line[1] == 'a':
        mask = line.split()[-1]
    else:
        bracket = line.index(']')
        integer = int(line.split()[-1])
        binary = str(bin(integer))[2:]
        while len(binary) < 36:
            binary = '0' + binary
        newBinary = ''
        for i in range(len(binary)-1,-1,-1):
            maskBit = mask[i]
            if maskBit == 'X':
                newBinary = binary[i] + newBinary
            elif maskBit == '0':
                newBinary = '0' + newBinary
            elif maskBit == '1':
                newBinary = '1' + newBinary
        integer = int(newBinary,2)
        mem[int(line[4:bracket])] = integer
total = 0
for i in mem:
    total += mem[i]
print(total)