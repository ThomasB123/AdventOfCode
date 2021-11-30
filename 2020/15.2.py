numbers = {0:0,3:1}#,6:2}
numbers = {10:0,16:1,6:2,0:3,1:4}#,17:5}
last = 17
nextNum = 0
for index in range(5,30000000-1):
    if last not in numbers:
        nextNum = 0
    else:
        nextNum = index-numbers[last]
    numbers[last] = index
    last = nextNum
print(nextNum)