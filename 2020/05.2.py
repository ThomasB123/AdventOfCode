infile = open('05input.txt','r')
lowest = 1023
highest = 0
ids = {}
for line in infile:
    lowRow = 0
    highRow = 127
    lowCol = 0
    highCol = 7
    for i in line[:7]:
        if i == 'B': lowRow = (lowRow+highRow)//2+1
        else: highRow = (lowRow+highRow)//2
    for i in line[7:-1]:
        if i == 'R': lowCol = (lowCol+highCol)//2+1
        else: highCol = (lowCol+highCol)//2
    idd = lowRow*8 + lowCol
    ids[idd] = None
    lowest = min(lowest,idd)
    highest = max(highest,idd)

for i in range(lowest,highest):
    if i not in ids:
        print(i)
        break