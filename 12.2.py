infile = open('12input.txt','r')
shipx = 0
shipy = 0
x = 10
y = 1
# NE is +ve
move = {'N':[0,1],'E':[1,0],'S':[0,-1],'W':[-1,0]}

def rotate(x,y,direction,amount):
    if x == y == 0:
        return x,y
    if amount == 180:
        return -x,-y
    if direction == 'R' and amount == 90 or direction == 'L' and amount == 270:
        return y,-x
    return -y,x

for line in infile:
    action,value = line[0],int(line[1:-1])
    if action == 'R' or action == 'L':
        x,y = rotate(x,y,action,value)
    elif action == 'F':
        shipx += x * value
        shipy += y * value
    else:
        x += move[action][0] * value
        y += move[action][1] * value
print(abs(shipx)+abs(shipy))