infile = open('05input.txt','r')
highest = 0
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
    highest = max(highest,lowRow*8+lowCol)
print(highest)