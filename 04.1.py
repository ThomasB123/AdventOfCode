infile = open('04input.txt','r')
count = 0
fields = []
check = {}
for line in infile:
    if line == '\n':
        for i in range(len(fields)):
            check[fields[i].split('\n')[0][:3]] = None
        count += len(check) == 8 or len(check) == 7 and 'cid' not in check
        fields = []
        check = {}
    else:
        fields.extend(line.split())
print(count)