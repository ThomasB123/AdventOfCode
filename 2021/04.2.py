inFile = open('04input.txt','r')
numbers = []
boards = []
check = []
for line in inFile:
    if len(line) > 15:
        for number in line[:-1].split(','):
            numbers.append(int(number))
    if line == '\n':
        boards.append([])
        check.append([])
    if 1 < len(line) < 16:
        row = line[:-1].split()
        boards[-1].append([])
        for r in row:
            boards[-1][-1].append(int(r))
        check[-1].append([0,0,0,0,0])

previousWinners = []
for i in range(len(check)):
    previousWinners.append(0)

def getWinners():
    won = []
    for i in range(len(check)):
        won.append(0)
        for j in range(5):
            if sum(check[i][j]) == 5:
                won[i] = 1
            column = 0
            for k in range(5):
                column += check[i][k][j]
            if column == 5:
                won[i] = 1
    return won

for count in range(len(numbers)):
    for i in range(len(boards)):
        for j in range(5):
            for k in range(5):
                if numbers[count] == boards[i][j][k]:
                    check[i][j][k] = 1
    winners = getWinners()
    if sum(winners) == len(winners):
        winner = previousWinners.index(0)
        unmarked = 0
        for i in range(5):
            for j in range(5):
                if not check[winner][i][j]:
                    unmarked += boards[winner][i][j]
        print(unmarked * numbers[count])
        break
    previousWinners = winners[:]