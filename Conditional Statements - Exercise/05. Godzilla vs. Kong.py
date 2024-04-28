budjet = float(input())
broiStatisti = int(input())
chenaOblekloStatist = float(input())

Dekor = budjet * 0.1
ChenaObleklo = chenaOblekloStatist * broiStatisti

if(broiStatisti >= 150 ):
    ChenaObleklo = ChenaObleklo * 0.9

Razhodi = Dekor + ChenaObleklo

if(Razhodi <= budjet):
    ostavashtiPari = budjet - Razhodi
    formatted_number = "{:.2f}".format(ostavashtiPari)
    print(f'Action!')
    print(f'Wingard starts filming with {formatted_number} leva left.')
else:
    ostavashtiPari = Razhodi - budjet
    formatted_number = "{:.2f}".format(ostavashtiPari)
    print(f'Not enough money!')
    print(f'Wingard needs {formatted_number} leva more.')