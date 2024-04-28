Bqdjet = float(input())
broiVideoCard = int(input())
broiProcessor = int(input())
broiRAM = int(input())

CENA_VIDEO = 250.00
CenaVideoCard = CENA_VIDEO * broiVideoCard
CenaProcessor = 0.35 * CenaVideoCard
CenaRAM = 0.1 * CenaVideoCard

Total = CenaVideoCard + (CenaProcessor * broiProcessor) + (CenaRAM * broiRAM)

if(broiVideoCard > broiProcessor):
    Total = Total * 0.85

Ostatuk = Bqdjet - Total
NujnaSuma = Total - Bqdjet
if(Bqdjet >= Total):
    print(f'You have {Ostatuk:.2f} leva left!')
else:
    print(f'Not enough money! You need {NujnaSuma:.2f} leva more!')