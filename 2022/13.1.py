infile = open('13input.txt','r')
pairs = [[]]
for line in infile:
    if line == '\n':
        pairs.append([])
    else:
        a = []
        index = [0]
        for char in line[1:-2]:
            toAppend = a
            for b in index[:-1]:
                toAppend = toAppend[b]
            if char == '[':
                toAppend.insert(index[-1],[])
                index.append(0)
            elif char == ']':
                index.pop()
            elif char == ',':
                index[-1] += 1
            elif char in '1234567890':
                if len(toAppend)-1 == index[-1]:
                    toAppend[index[-1]] = int(char)+toAppend[index[-1]]*10
                else:
                    toAppend.insert(index[-1],int(char))
        pairs[-1].append(a)
def compare(a,b):
    if len(a) == 0:
        return True
    elif len(b) == 0:
        return False
    if isinstance(a[0],int) and isinstance(b[0],int):
        if a[0] < b[0]:
            return True
        elif a[0] > b[0]:
            return False
    elif isinstance(a[0],int) and isinstance(b[0],list):
        return compare([[a[0]],a[1:]],b)
    elif isinstance(a[0],list) and isinstance(b[0],int):
        return compare(a,[[b[0]],b[1:]])
    elif isinstance(a[0],list) and isinstance(b[0],list):
        if a[0] != b[0]:
            return compare(a[0],b[0])
    if len(a) == 1:
        return True
    elif len(b) == 1:
        return False
    return compare(a[1:],b[1:])
out = 0
for i in range(len(pairs)):
    out += compare(pairs[i][0],pairs[i][1]) * (i+1)
print(out)
