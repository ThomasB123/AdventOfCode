infile = open('04input.txt','r')
grid, removed, total, neighbours = [], True, 0, [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for line in infile: grid.append(list(line[:-1]))
while removed:
    removed = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                rolls = 0
                for x, y in neighbours:
                    new_i, new_j = i+x, j+y
                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[i]) and grid[new_i][new_j] == '@': rolls += 1
                if rolls < 4:
                    total += 1
                    removed = True
                    grid[i][j] = '.'
print(total)
