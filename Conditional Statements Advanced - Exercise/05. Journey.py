bqdjet = float(input())
sezon = input()

krainaCena = 0.00
destinaciq = str()
mqsto = str()

if bqdjet <= 100:
    destinaciq = "Bulgaria"

    if sezon == "summer":
        mqsto = "Camp"
        krainaCena = bqdjet * 0.3
    elif sezon == "winter":
        mqsto = "Hotel"
        krainaCena = bqdjet * 0.7
elif 100 < bqdjet <= 1000:
    destinaciq = "Balkans"

    if sezon == "summer":
        mqsto = "Camp"
        krainaCena = bqdjet * 0.4
    elif sezon == "winter":
        mqsto = "Hotel"
        krainaCena = bqdjet * 0.8
elif bqdjet > 1000:
    destinaciq = "Europe"
    mqsto = "Hotel"
    krainaCena = bqdjet * 0.9

print(f"Somewhere in {destinaciq}")
print(f"{mqsto} - {krainaCena:.2f}")