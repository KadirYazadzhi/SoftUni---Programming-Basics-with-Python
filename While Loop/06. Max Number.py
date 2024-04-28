maxNumber = -100000000

while True:
    num = input()

    if num == "Stop":
        print(maxNumber)
        break

    number = int(num)

    if number > maxNumber:
        maxNumber = number