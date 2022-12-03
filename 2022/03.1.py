infile = open('03input.txt','r')
out = 0
for line in infile:
    shared = ord(set(line[:len(line)//2]).intersection(line[len(line)//2:-1]).pop())
    if shared < 91:
        out += shared - 38
    else:
        out += shared - 96
print(out)
