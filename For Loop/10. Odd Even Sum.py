n = int(input())

numbersEven = []
numbersOdd = []

for i in range (0, n ):
    number = int(input())

    if i % 2 == 0:
        numbersEven.append(number)
    else:
        numbersOdd.append(number)

even = sum(numbersEven)
odd = sum(numbersOdd)

if even == odd:
    print(f'Yes')
    print(f'Sum = {even}')
else:
    if even > odd:
        sum = even - odd
        print(f'No')
        print(f'Diff = {sum}')
    else:
        sum = odd - even
        print(f'No')
        print(f'Diff = {sum}')