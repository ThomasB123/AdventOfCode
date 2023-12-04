infile = open('02input.txt','r')
out = 0
for line in infile:
    words = (line[:-1] + ',').split()
    minimum = {'red': 0, 'green': 0, 'blue': 0}
    for i in range(2, len(words)-1, 2):
        minimum[words[i+1][:-1]] = max(int(words[i]), minimum[words[i+1][:-1]])
    out += minimum['red'] * minimum['green'] * minimum['blue']
print(out)
