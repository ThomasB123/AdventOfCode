infile = open('01input.txt','r')
match = {}
for line in infile:
    number = int(line[:-1])
    if number in match:
        print(number*(2020-number))
        break
    match[2020-number] = None