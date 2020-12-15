infile = open('12input.txt','r')
x = 0
y = 0
direction = 90
# NE is +ve
compass = {0:'N',90:'E',180:'S',270:'W'}
move = {'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,0]}
for line in infile:
    action,value = line[0],int(line[1:-1])
    if action == 'R':
        direction = (direction + value) % 360
    elif action == 'L':
        direction = (direction-value) % 360
    else:
        if action == 'F':
            action = compass[direction]
        x += move[action][0] * value
        y += move[action][1] * value
print(abs(x)+abs(y))