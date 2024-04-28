bqdjet = int(input())
sezon = input()
broiRibari = int(input())

prolet = 3000
esenLqto = 4200
zima = 2600

krainaCena = 0.00

if sezon == "Spring":
    krainaCena = prolet
elif sezon == "Summer" or sezon == "Autumn":
    krainaCena = esenLqto
elif sezon == "Winter":
    krainaCena = zima

if broiRibari <= 6:
    krainaCena *= 0.9
elif 6 < broiRibari <= 11:
    krainaCena *= 0.85
elif broiRibari >= 12:
    krainaCena *= 0.75

if broiRibari % 2 == 0 and sezon != "Autumn":
    krainaCena *= 0.95

if krainaCena <= bqdjet:
    Total = "{:.2f}".format(bqdjet - krainaCena)
    print(f"Yes! You have {Total} leva left.")
else:
    Total = "{:.2f}".format(krainaCena - bqdjet)
    print(f"Not enough money! You need {Total} leva.")