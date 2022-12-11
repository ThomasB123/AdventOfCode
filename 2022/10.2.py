infile = open('10input.txt','r')
x = 1
cycle = 0
screen = [[] for i in range(6)]
for line in infile:
    cycle += 1
    if x <= cycle % 40 <= x+1 or (x+2) % 40 == cycle % 40:
        screen[(cycle-1)//40].append('#')
    else:
        screen[(cycle-1)//40].append('.')
    if line[0] == "a":
        cycle += 1
        if x <= cycle % 40 <= x+1 or (x+2) % 40 == cycle % 40:
            screen[(cycle-1)//40].append('#')
        else:
            screen[(cycle-1)//40].append('.')
        x += int(line.split()[1])
for i in screen:
    print(''.join(i))
