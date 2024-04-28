number = int(input())
Bonus = int()
NewNumber = int()

if number <= 100:
    Bonus = 5

elif number > 1000:
    Bonus = number * 0.1

else:
    Bonus = number * 0.2

if number % 2 == 0:
    Bonus += 1

elif number % 10 == 5:
    Bonus += 2

NewNumber = number + Bonus
print(Bonus)
print(NewNumber)