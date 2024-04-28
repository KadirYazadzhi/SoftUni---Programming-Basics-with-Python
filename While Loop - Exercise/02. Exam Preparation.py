average = 0
last = ""
poorGrade = 0
all = 0

countPoorGrade = int(input())

while True:
    predmet = input()
    if predmet == "Enough":
        score = average / all if all > 0 else 0
        print(f'Average score: {score:.2f}')
        print(f'Number of problems: {all}')
        print(f'Last problem: {last}')
        break
    grade = float(input())

    average += grade
    if grade <= 4:
        poorGrade += 1
    if poorGrade >= countPoorGrade:
        print(f'You need a break, {poorGrade} poor grades.')
        break

    all += 1
    last = predmet