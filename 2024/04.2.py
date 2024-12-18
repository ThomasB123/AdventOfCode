infile = open('04input.txt')

grid = []
for line in infile:
    grid.append(line.strip())

total = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):
        total += grid[i][j] + grid[i+1][j+1] + grid[i+1][j-1] + grid[i-1][j-1] + grid[i-1][j+1] in ['ASMMS', 'ASSMM', 'AMMSS', 'AMSSM']
print(total)
