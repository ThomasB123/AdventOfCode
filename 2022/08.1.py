infile = open('08input.txt','r')
trees = []
count = 0
for line in infile:
    trees.append([])
    for char in line[:-1]:
        trees[-1].append(int(char))
width = len(trees)
for i in range(width):
    for j in range(width):
        height = trees[i][j]
        column = []
        for k in range(width):
            column.append(trees[k][j])
        if i==0 or j==0 or i==width-1 or j==width-1 or height>max(trees[i][j+1:]) or height>max(trees[i][:j]) or height>max(column[i+1:]) or height>max(column[:i]):
            count += 1
print(count)
