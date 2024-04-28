minNumber = 100000000

while True:
    num = input()

    if num == "Stop":
        print(minNumber)
        break

    number = int(num)

    if number < minNumber:
        minNumber = number