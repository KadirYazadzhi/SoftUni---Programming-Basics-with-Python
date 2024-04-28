BroiPileshkiMenuta = int(input())
BroiRibeniMenuta = int(input())
BroiVegetarianskiMenuta = int(input())

PILESHKO = 10.35
RIBA = 12.40
VEGAN = 8.15
DOSTAVKA = 2.50
DESERT = 20

ChenaPileshko = BroiPileshkiMenuta * PILESHKO
ChenaRiba = BroiRibeniMenuta * RIBA
ChenaVegan = BroiVegetarianskiMenuta * VEGAN

Desert = ((ChenaPileshko + ChenaRiba + ChenaVegan) * 20) / 100
Total = ChenaPileshko + ChenaRiba + ChenaVegan + Desert + DOSTAVKA

print(Total)