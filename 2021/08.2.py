inFile = open('08input.txt','r')
outputs = []
for line in inFile:
    outputs.append(line[:-1].split(' | '))

translate = ['','','','','','','','','','']

total = 0
for i in outputs:
    numbers = i[0].split()
    for j in range(len(numbers)):
        numbers[j] = ''.join(sorted(numbers[j]))
    for j in numbers:
        if len(j) == 2:
            translate[1] = j
        elif len(j) == 4:
            translate[4] = j
        elif len(j) == 3:
            translate[7] = j
        elif len(j) == 7:
            translate[8] = j
    for j in numbers:
        if len(j) == 6:
            for k in 'abcdefg':
                if k not in j:
                    if k in translate[1]:
                        translate[6] = j
                        six = k
                    elif k in translate[4]:
                        translate[0] = j
                    else:
                        translate[9] = j
    for j in numbers:
        if len(j) == 5:
            missing = ''
            for k in 'abcdefg':
                if k not in j:
                    missing += k
            if missing[0] not in translate[1] and missing[1] not in translate[1]:
                translate[3] = j
            elif six in missing:
                translate[5] = j
            else:
                translate[2] = j
    output = i[1].split()
    number = ''
    for j in range(len(output)):
        output[j] = ''.join(sorted(output[j]))
        number += str(translate.index(output[j]))
    total += int(number)

print(total)
