NailonMetri = int(input())
BoqLitri = int(input())
RazreditelLitri = int(input())
ChasoveRabota = int(input())

NAILON = 1.50
BOQ = 14.50
RAZREDITEL = 5.00

DOPULNITELNO_BOQ = 1.1
NAILON_DOPULNITELNO = 2
TORBICHKI = 0.40

Rabota = 30

ChenaNailon = (NailonMetri + 2) * NAILON
ChenaBoq = BoqLitri * BOQ * DOPULNITELNO_BOQ
ChenaRazreditel = RazreditelLitri * RAZREDITEL

TotalMateriali = ChenaNailon + ChenaBoq + ChenaRazreditel + TORBICHKI
ChenaRabota = ((TotalMateriali * Rabota) / 100) * ChasoveRabota

Total = TotalMateriali + ChenaRabota

print("{:.2f}".format(Total))