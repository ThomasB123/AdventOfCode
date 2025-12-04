infile = open('03input.txt','r')
total = 0
for line in infile:
    bank = list(map(int, line[:-1]))
    joltage = 0
    for i in range(11):
        biggest = max(bank[:i-11])
        joltage = joltage * 10 + biggest
        bank = bank[bank.index(biggest)+1:]
    total += joltage * 10 + max(bank)
print(total)
