startHours = int(input())
startMinutes = int(input())

timeInMinutes = int(startHours * 60 + startMinutes)
MinutesPlus15 = int(timeInMinutes + 15)

finalHours = int(MinutesPlus15 / 60)
finalMinutes = int(MinutesPlus15 % 60)

if finalHours >= 24:
    finalHours -= 24

if finalMinutes < 10:
    print(f'{finalHours}:0{finalMinutes}')
else:
    print(f'{finalHours}:{finalMinutes}')