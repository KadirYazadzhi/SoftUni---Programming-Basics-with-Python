numberBrowser = int(input())
salary = int(input())

FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

for i in range(numberBrowser):
    browserName = input()

    if browserName == "Facebook":
        salary -= FACEBOOK
    elif browserName == "Instagram":
        salary -= INSTAGRAM
    elif browserName == "Reddit":
        salary -= REDDIT
    else:
        salary = salary

    if salary <= 0:
        break

if salary <= 0:
    print(f'You have lost your salary.')

else:
    print(f'{salary}')