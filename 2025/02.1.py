infile = open('02input.txt','r')
sum = 0
for line in infile:
    ranges = line.split(",")
    for i in ranges:
        a, b = map(int, i.split("-"))
        for j in range(a, b+1):
            if len(str(j)) % 2 == 0:
                if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]: sum += j
print(sum)
