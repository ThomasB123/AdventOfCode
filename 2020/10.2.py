import math
infile = open('10input.txt','r')
adapters = []
for line in infile:
    adapters.append(int(line))
adapters.sort()

last = 0
minus = {1:0,2:0,3:0,4:1}
inaRow = 0
count = 1
multi = 0
for x in range(len(adapters)):
    if adapters[x] - last == 1:
        inaRow += 1
    else:
        if inaRow > 1:
            multi = 0
            for i in range(0,inaRow):
                multi += math.comb(inaRow-1,i)
            multi -= minus[inaRow]
            count *= multi
        inaRow = 0
    last = adapters[x]
if inaRow > 1:
    multi = 0
    for i in range(0,inaRow):
        multi += math.comb(inaRow-1,i)
    multi -= minus[inaRow]
    count *= multi

print(count)