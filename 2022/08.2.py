infile = open('08input.txt','r')
trees = []
visible = []
for line in infile:
    trees.append([])
    for char in line[:-1]:
        trees[-1].append(int(char))
width = len(trees)
for i in range(width):
    for j in range(width):
        height = trees[i][j]
        up = 0
        for k in range(i-1,-1,-1):
            up += 1
            if trees[k][j] >= height: break
        down = 0
        for k in range(i+1,width):
            down += 1
            if trees[k][j] >= height: break
        left = 0
        for k in range(j-1,-1,-1):
            left += 1
            if trees[i][k] >= height: break
        right = 0
        for k in range(j+1,width):
            right += 1
            if trees[i][k] >= height: break
        visible.append(up*down*left*right)
print(max(visible))
