from math import pi

figures = input()

if figures == 'square':
    a = float(input())
    area = a * a
    print(round(area, 3))

elif figures == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
    print(round(area, 3))

elif figures == 'circle':
    r = float(input())
    area = r * r * pi
    print(round(area, 3))

elif figures == 'triangle':
    a = float(input())
    h = float(input())
    area = (a * h) / 2
    print(round(area, 3))