infile = open('08input.txt','r')
instructions = []
for line in infile:
    instructions.append(line.split())

found = False
change = 0
while not found:
    change += 1
    seen = {}
    acc = 0
    jmp = 0
    while jmp not in seen:
        seen[jmp] = None
        operation,argument = instructions[jmp]
        if jmp == change:
            if operation == 'jmp':
                operation = 'nop'
            elif operation == 'nop':
                operation = 'jmp'
        if operation == 'acc':
            if argument[0] == '+':
                acc += int(argument[1:])
            else:
                acc -= int(argument[1:])
            jmp += 1
        elif operation == 'jmp':
            if argument[0] == '+':
                jmp += int(argument[1:])
            else:
                jmp -= int(argument[1:])
        elif operation == 'nop':
            jmp += 1
        if jmp == len(instructions)-1:
            found = True
            break
print(acc)