vid = input()
red = int(input())
kolona = int(input())

PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

sborSedalki = red * kolona
if vid == "Premiere":
    print(f'{sborSedalki * PREMIERE:.2f} leva')
elif vid == "Normal":
    print(f'{sborSedalki * NORMAL:.2f} leva')
elif vid == "Discount":
    print(f'{sborSedalki * DISCOUNT:.2f} leva')