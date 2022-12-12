infile = open('12input.txt','r')
h = []
fastest = {}
a = -1
for line in infile:
    b = -1
    a += 1
    h.append([])
    for char in line[:-1]:
        b += 1
        h[-1].append(char)
        if char == 'S':
            fastest[(a,b)] = 0
            # x,y,height,length
            s = [[a,b,1,0]]
        else:
            fastest[(a,b)] = 1000000
height = len(h)
width = len(h[0])
while h[s[0][0]][s[0][1]] != 'E':
    i,j = s[0][0],s[0][1]
    for x in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0 <= x[0] < height and 0 <= x[1] < width:
            char = h[x[0]][x[1]]
            if s[0][2] > 25 and char == 'E':
                print(s[0][3]+1)
                exit()
            if s[0][3]+1 < fastest[x] and 97 <= ord(char) <= s[0][2] + 97:
                    fastest[x] = s[0][3]+1
                    s.append([x[0],x[1],ord(char)-96,s[0][3]+1])
    s.pop(0)
