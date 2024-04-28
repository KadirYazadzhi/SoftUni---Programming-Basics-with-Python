PUZEL = 2.60
KYKLA = 3.00
MECHE = 4.10
MINION = 8.20
KAMIONCHE = 2

ChenaEkskurziq = float(input())
broiPuzeli = int(input())
broiKykli = int(input())
broiMecheta = int(input())
broiMinioni = int(input())
broiKamioni = int(input())

TotalChena = (broiPuzeli * PUZEL) + (broiKykli * KYKLA) + (broiMecheta * MECHE) + (broiMinioni * MINION) + (broiKamioni * KAMIONCHE)
ObshtoIgrachki = broiPuzeli + broiKykli + broiMecheta + broiMinioni + broiKamioni

if ObshtoIgrachki >= 50:
    TotalChena = TotalChena * 0.75

TotalChena = TotalChena * 0.9

Pari = TotalChena - ChenaEkskurziq
if (ChenaEkskurziq <= TotalChena):
    formatted_number = "{:.2f}".format(Pari)
    print(f'Yes! {formatted_number} lv left.')
else:
    Pari = ChenaEkskurziq - TotalChena
    formatted_number = "{:.2f}".format(Pari)
    print(f'Not enough money! {formatted_number} lv needed.')