number1 = int(input())
number2 = int(input())
operator = input()

rezultat = 0.00
oddOrEven = str()

if operator == "+":
    rezultat = number1 + number2
    if rezultat % 2 == 0:
      oddOrEven = "even"
    else:
        oddOrEven = "odd"
    print(f"{number1} + {number2} = {rezultat} - {oddOrEven}")

elif operator == "-":
    rezultat = number1 - number2
    if rezultat % 2 == 0:
        oddOrEven = "even"
    else:
        oddOrEven = "odd"
    print(f"{number1} - {number2} = {rezultat} - {oddOrEven}")

elif operator == "*":
    rezultat = number1 * number2
    if rezultat % 2 == 0:
        oddOrEven = "even"
    else:
        oddOrEven = "odd"
    print(f"{number1} * {number2} = {rezultat} - {oddOrEven}")

if number2 != 0:
    if operator == "/":
        rezultat = "{:.2f}".format(number1 / number2)
        print(f"{number1} / {number2} = {rezultat}")

    elif operator == "%":
        rezultat = number1 % number2
        print(f"{number1} % {number2} = {rezultat}")
else:
    print(f"Cannot divide {number1} by zero")