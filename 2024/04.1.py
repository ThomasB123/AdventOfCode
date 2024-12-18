infile = open('04input.txt')

grid = []
for line in infile:
    grid.append(line.strip())

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        total += grid[i][j:j+4] == 'XMAS'
        total += grid[i][j-3:j+1] == 'SAMX'
        total += ''.join([row[j] for row in grid[i:i+4] if row]) == 'XMAS'
        total += ''.join([row[j] for row in grid[i-3:i+1] if row]) == 'SAMX'
        total += i+3 < len(grid) and j+3 < len(grid[i]) and ''.join([grid[i+x][j+x] for x in range(4)]) == 'XMAS'
        total += i-3 >= 0 and j-3 >= 0 and ''.join([grid[i-x][j-x] for x in range(4)]) == 'XMAS'
        total += i-3 >= 0 and j+3 < len(grid[i]) and ''.join([grid[i-x][j+x] for x in range(4)]) == 'XMAS'
        total += i+3 < len(grid) and j-3 >= 0 and ''.join([grid[i+x][j-x] for x in range(4)]) == 'XMAS'
print(total)
