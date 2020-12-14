infile = open('01input.txt','r')
match = {}
numbers = {}
for line in infile:
    number = int(line)
    match[2020-number] = None
    numbers[number] = None

match2 = {}
for number in match:
    for otherNumber in numbers:
        if otherNumber in match2 and number-otherNumber in numbers:
            print(otherNumber*(2020-number)*(number-otherNumber))
            break
        match2[number-otherNumber] = None
