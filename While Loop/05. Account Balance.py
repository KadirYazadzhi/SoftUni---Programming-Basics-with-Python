total = 0

while True:
    suma = input()

    if suma == "NoMoreMoney":
        print(f'Total: {total:.2f}')
        break
    elif float(suma) < 0:
        print(f'Invalid operation!')
        print(f'Total: {total:.2f}')
        break
    else:
        suma = float(suma)
        print(f'Increase: {suma:.2f}')
        total += float(suma)