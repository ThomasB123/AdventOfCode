infile = open('02input.txt','r')
sum = 0
for line in infile:
    ranges = line.split(",")
    for i in ranges:
        a, b = map(int, i.split("-"))
        for j in range(a, b+1):
            for k in range(2, len(str(j))+1):
                if len(str(j)) % k == 0:
                    matching = True
                    split =len(str(j)) // k
                    pattern = str(j)[:split]
                    for l in range(1, k):
                        if pattern != str(j)[split*l:split*(l+1)]:
                            matching = False
                            break
                    if matching:
                        sum += j
                        break
print(sum)
