infile = open('01input.txt','r')
digits = ['oneight','twone','eightwo','one','two','three','four','five','six','seven','eight','nine']
numbers = ['18','21','82','1','2','3','4','5','6','7','8','9']
out = 0
for line in infile:
    number = ''
    for i in range(12):
        line = line.replace(digits[i], numbers[i])
    for char in line:
        if char.isdigit():
            if number == '':
                number = char
            digit = char
    out += int(number + digit)
print(out)
