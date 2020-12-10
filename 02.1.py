infile = open('02input.txt','r')
count = 0
for line in infile:
    rang,chara,passw = line.split(' ')
    mini,maxi = rang.split('-')
    mini = int(mini)
    maxi = int(maxi)
    chara = chara[0]
    count += mini <= passw.count(chara) <= maxi
print(count)