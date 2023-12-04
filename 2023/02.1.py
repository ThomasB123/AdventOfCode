infile = open('02input.txt','r')
out, game = 0, 1
limits = {'red': 12, 'green': 13, 'blue': 14}
for line in infile:
    words = (line[:-1] + ',').split()
    possible = True
    for i in range(2, len(words)-1, 2):
        if int(words[i]) > limits[words[i+1][:-1]]:
            possible = False
    if possible:
        out += game
    game += 1
print(out)
