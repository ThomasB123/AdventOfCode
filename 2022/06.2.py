infile = open('06input.txt','r')
start = 0
end = 13
buffer = ''
for line in infile:
    buffer = line[:-1]

while end < len(buffer):
    fourteen = buffer[start:end+1]
    out = True
    for i in fourteen:
        if fourteen.count(i) > 1:
            out = False
            break
    if out:
        print(end+1)
        exit()
    start += 1
    end += 1
