infile = open('02input.txt','r')
count = 0
for line in infile:
    rang,chara,passw = line.split(' ')
    first,last = rang.split('-')
    first = int(first)
    last = int(last)
    chara = chara[0]
    count += passw[first-1] == chara != passw[last-1] or passw[first-1] != chara == passw[last-1]
print(count)