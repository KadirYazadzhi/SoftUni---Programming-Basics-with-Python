n = int(input())

numbers = []

maxnumber = 0
allnumber = 0
for i in range(n):
    number = int(input())
    if number > maxnumber:
        maxnumber = number
    numbers.append(number)

allnumber = sum(numbers)

if maxnumber == allnumber / 2:
    print('Yes')
    print(f'Sum = {allnumber - maxnumber}')
else:
    print('No')
    print(f'Diff = {abs(maxnumber - (allnumber - maxnumber))}')