infile = open('01input.txt','r')
match = {}
numbers = {}
for line in infile:
    number = int(line)
    match[2020-number] = None
    numbers[number] = None

match2 = {}
found = False
for number in match:
    for otherNumber in numbers:
        if otherNumber in match2 and number-otherNumber in numbers:
            found = True
            break
        match2[number-otherNumber] = None
    if found:
        break
print(otherNumber*(2020-number)*(number-otherNumber))