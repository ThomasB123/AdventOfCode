numbers = [0,3,6]
numbers = [10,16,6,0,1,17]
for i in range(2020-len(numbers)):
    if numbers[-1] not in numbers[:-1]:
        numbers.append(0)
    else:
        count = 1
        while numbers[len(numbers)-count-1] != numbers[-1]:
            count += 1
        numbers.append(count)
print(numbers[-1])