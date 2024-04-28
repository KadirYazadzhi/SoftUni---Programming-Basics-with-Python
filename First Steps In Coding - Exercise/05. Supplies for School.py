broiHimikali = int(input())
broiMarkeri = int(input())
litriPreparat = int(input())
ProcentNamalenie = int(input())

ChenaHimikali = 5.80
ChenaMarkeri = 7.20
ChenaPreparat = 1.20

ObshtaCenaHimikali = ChenaHimikali * broiHimikali
ObshtaCenaMarkeri = ChenaMarkeri * broiMarkeri
ObshtaCenaPreparat = ChenaPreparat * litriPreparat

Namalenie = (100 - ProcentNamalenie) / 100
Total = (ObshtaCenaHimikali + ObshtaCenaMarkeri + ObshtaCenaPreparat) * Namalenie

print(Total)