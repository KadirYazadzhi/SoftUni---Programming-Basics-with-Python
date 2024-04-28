product = input()
town = input()
number = float(input())

if town == "Sofia":
    if product == "coffee":
        coffee = 0.50
        Total = coffee * number
    elif product == "water":
        water = 0.80
        Total = water * number
    elif product == "beer":
        beer = 1.20
        Total = beer * number
    elif product == "sweets":
        sweets = 1.45
        Total = sweets * number
    elif product == "peanuts":
        peanuts = 1.60
        Total = peanuts * number
elif town == "Plovdiv":
    if product == "coffee":
        coffee = 0.40
        Total = coffee * number
    elif product == "water":
        water = 0.70
        Total = water * number
    elif product == "beer":
        beer = 1.15
        Total = beer * number
    elif product == "sweets":
        sweets = 1.30
        Total = sweets * number
    elif product == "peanuts":
        peanuts = 1.50
        Total = peanuts * number
elif town == "Varna":
    if product == "coffee":
        coffee = 0.45
        Total = coffee * number
    elif product == "water":
        water = 0.70
        Total = water * number
    elif product == "beer":
        beer = 1.10
        Total = beer * number
    elif product == "sweets":
        sweets = 1.35
        Total = sweets * number
    elif product == "peanuts":
        peanuts = 1.55
        Total = peanuts * number

print(Total)