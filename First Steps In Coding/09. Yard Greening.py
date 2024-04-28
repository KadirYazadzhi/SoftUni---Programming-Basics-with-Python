KvadratniMetri = float(input())

CHENA_NA_METUR = 7.61
OTSTUPKA_ZA_KRAINA_CENA = 0.82
OTSTUPKA = 0.18

finalPrice = (KvadratniMetri * CHENA_NA_METUR) * OTSTUPKA_ZA_KRAINA_CENA
otstupkaOtChenata = (KvadratniMetri * CHENA_NA_METUR) * OTSTUPKA

print(f'The final price is: {finalPrice} lv.')
print(f'The discount is: {otstupkaOtChenata} lv.')