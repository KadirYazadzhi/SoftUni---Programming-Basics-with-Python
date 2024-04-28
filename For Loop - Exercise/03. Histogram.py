n = int(input())

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

for i in range(n):
    number = int(input())

    if number < 200:
        counter1 += 1
    elif 200 <= number < 400:
        counter2 += 1
    elif 400 <= number < 600:
        counter3 += 1
    elif 600 <= number < 800:
        counter4 += 1
    else:
        counter5 += 1

allcounter = float(counter1 + counter2 + counter3 + counter4 + counter5)

procent1 = float(counter1 / allcounter * 100)
print(f'{procent1:.2f}%')
procent2 = float(counter2 / allcounter * 100)
print(f'{procent2:.2f}%')
procent3 = float(counter3 / allcounter * 100)
print(f'{procent3:.2f}%')
procent4 = float(counter4 / allcounter * 100)
print(f'{procent4:.2f}%')
procent5 = float(counter5 / allcounter * 100)
print(f'{procent5:.2f}%')
