suma = float(input())
srok = int(input())
lihvenProcent = float(input())

lihva = suma * lihvenProcent / 100
lihvaMesec = lihva / 12

obshtaSuma = suma + lihvaMesec * srok

print(obshtaSuma)