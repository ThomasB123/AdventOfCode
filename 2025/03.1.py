infile = open('03input.txt','r')
total = 0
for line in infile:
    bank = list(map(int, line[:-1]))
    first = max(bank[:-1])
    second = max(bank[bank.index(first)+1:])
    total += first * 10 + second
print(total)
