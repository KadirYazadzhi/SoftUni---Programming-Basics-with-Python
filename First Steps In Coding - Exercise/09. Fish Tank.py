Duljina = int(input())
Shirochina = int(input())
Visochina = int(input())
Procent = float(input())

Obem = Duljina * Shirochina * Visochina
ObemLitri = Obem / 1000

ZaetoProstranstvo = Procent / 100

NujniLitri = ObemLitri * (1 - ZaetoProstranstvo)

print(NujniLitri)