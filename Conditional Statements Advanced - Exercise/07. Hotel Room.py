month = input()
day = int(input())

apartment = 0.00
studio = 0.00
TotalApartment = 0.00
TotalStudio = 0.00

if month == "May" or month == "October":
    apartment = 65.00
    studio = 50.00
    if day > 14:
        studio *= 0.7
        apartment *= 0.9
    elif day > 7:
        studio *= 0.95

elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    if day > 14:
        studio *= 0.8
        apartment *= 0.9

elif month == "July" or month == "August":
    apartment = 77
    studio = 76
    if day > 14:
        apartment *= 0.9

TotalApartment = apartment * day
TotalStudio = studio * day

print(f"Apartment: {TotalApartment:.2f} lv.")
print(f"Studio: {TotalStudio:.2f} lv.")