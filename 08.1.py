infile = open('08input.txt','r')
instructions = []
for line in infile:
    instructions.append(line.split())

seen = {}
acc = 0
jmp = 0
while jmp not in seen:
    seen[jmp] = None
    operation,argument = instructions[jmp]
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
print(acc)