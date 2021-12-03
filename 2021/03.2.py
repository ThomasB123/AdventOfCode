infile = open('03input.txt','r')
numbers = []
oxygen = []
co2 = []
for line in infile:
    numbers.append(line[:-1])
    oxygen.append(line[:-1])
    co2.append(line[:-1])

def popular(array, bit, most):
    count = 0
    zeros = []
    ones = []
    for number in array:
        if number[bit] == '1':
            ones.append(number)
        else:
            zeros.append(number)
    if most and len(ones) > len(zeros) or not most and len(ones) < len(zeros) or most and len(ones) == len(zeros):
        return ones
    return zeros

bit = 0
while len(oxygen) > 1:
    oxygen = popular(oxygen,bit,True)
    bit += 1

bit = 0
while len(co2) > 1:
    co2 = popular(co2,bit,False)
    bit += 1

o = 0
c = 0
mult = 1
for i in range(len(oxygen[0])-1,-1,-1):
    o += int(oxygen[0][i]) * mult
    c += int(co2[0][i]) * mult
    mult *= 2

print(o*c)