n = int(input())
numbers = []
suma = 0

while n > suma:
    number = int(input())
    numbers.append(number)
    suma = sum(numbers)
    if suma >= n:
        break

print(suma)