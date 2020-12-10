infile = open('03input.txt','r')
index1 = index2 = index3 = index4 = index5 = 0
count1 = count2 = count3 = count4 = count5 = 0
for line in infile:
    count1 += line[index1] == '#'
    count2 += line[index2] == '#'
    count3 += line[index3] == '#'
    count4 += line[index4] == '#'
    if index5 % 1 == 0:
        index5 = int(index5)
        count5 += line[index5] == '#'
    index1 = (index1 + 1) % (len(line)-1)
    index2 = (index2 + 3) % (len(line)-1)
    index3 = (index3 + 5) % (len(line)-1)
    index4 = (index4 + 7) % (len(line)-1)
    index5 = (index5 + 0.5) % (len(line)-1)
print(count1*count2*count3*count4*count5)