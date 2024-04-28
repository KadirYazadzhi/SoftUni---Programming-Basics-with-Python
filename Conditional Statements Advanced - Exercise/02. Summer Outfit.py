gradusi = int(input())
vreme = input()

if vreme == "Morning":
    if 10 <= gradusi <= 18:
        print(f"It's {gradusi} degrees, get your Sweatshirt and Sneakers.")
    elif 18 < gradusi <= 24:
        print(f"It's {gradusi} degrees, get your Shirt and Moccasins.")
    elif gradusi >= 25:
        print(f"It's {gradusi} degrees, get your T-Shirt and Sandals.")
elif vreme == "Afternoon":
    if 10 <= gradusi <= 18:
        print(f"It's {gradusi} degrees, get your Shirt and Moccasins.")
    elif 18 < gradusi <= 24:
        print(f"It's {gradusi} degrees, get your T-Shirt and Sandals.")
    elif gradusi >= 25:
        print(f"It's {gradusi} degrees, get your Swim Suit and Barefoot.")
elif vreme == "Evening":
    print(f"It's {gradusi} degrees, get your Shirt and Moccasins.")