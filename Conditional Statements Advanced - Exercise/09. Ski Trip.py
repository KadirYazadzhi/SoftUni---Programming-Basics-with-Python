day = int(input())
roomType = input()
rating =input()

roomPrice = 0.00
Total = 0.00
if roomType == "room for one person":
    roomPrice = 18.00
    Total = (day - 1) * roomPrice

elif roomType == "apartment":
    roomPrice = 25.00
    Total = (day - 1) * roomPrice

    if day < 10:
        Total *= 0.7
    elif 10 < day <= 15:
        Total *= 0.65
    elif day > 15:
        Total *= 0.5

elif roomType == "president apartment":
    roomPrice = 35.00
    Total = (day - 1) * roomPrice

    if day < 10:
        Total *= 0.9
    elif 10 < day <= 15:
        Total *= 0.85
    elif day > 15:
        Total *= 0.8

if rating == "positive":
    Total *= 1.25
elif rating == "negative":
    Total *= 0.9

print(f"{Total:.2f}")