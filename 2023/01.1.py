infile = open('01input.txt','r')
out = 0
for line in infile:
    number = ''
    for char in line:
        if char.isdigit():
            if number == '':
                number = char
            digit = char
    out += int(number + digit)
print(out)
