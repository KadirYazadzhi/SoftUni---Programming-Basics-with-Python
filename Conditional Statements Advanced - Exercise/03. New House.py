vidCvete = input()
broiCvetq = int(input())
bqdjet = float(input())

ROSES = 5.00
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3.00
GLADIOLUS = 2.50

krainaCena = 0.00
if vidCvete == "Roses":
    krainaCena = broiCvetq * ROSES
    if broiCvetq > 80:
        krainaCena *= 0.9

elif vidCvete == "Dahlias":
    krainaCena = broiCvetq * DAHLIAS
    if broiCvetq > 90:
        krainaCena *= 0.85

elif vidCvete == "Tulips":
    krainaCena = broiCvetq * TULIPS
    if broiCvetq > 80:
        krainaCena *= 0.85

elif vidCvete == "Narcissus":
    krainaCena = broiCvetq * NARCISSUS
    if broiCvetq < 120:
        krainaCena *= 1.15

elif vidCvete == "Gladiolus":
    krainaCena = broiCvetq * GLADIOLUS
    if broiCvetq < 80:
        krainaCena *= 1.20

if bqdjet >= krainaCena:
    Total = "{:.2f}".format(bqdjet - krainaCena)
    print(f"Hey, you have a great garden with {broiCvetq} {vidCvete} and {Total} leva left.")
else:
    Total = "{:.2f}".format(krainaCena - bqdjet)
    print(f"Not enough money, you need {Total} leva more.")
