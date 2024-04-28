n = int(input())

numbersleft = []
numbersright = []
for i in range (0, n * 2):
    number = int(input())

    if i < n:
        numbersleft.append(number)
    else:
        numbersright.append(number)

numberInLeft = sum(numbersleft)
numberInRight = sum(numbersright)

if numberInLeft == numberInRight:
    print(f'Yes, sum = {numberInLeft} ')
else:
    if numberInLeft < numberInRight:
        sum = numberInRight - numberInLeft
        print(f'No, diff = {sum}')
    else:
        sum = numberInLeft - numberInRight
        print(f'No, diff = {sum}')