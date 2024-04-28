input_text = input()
a = 1
e = 2
i = 3
o = 4
u = 5
sum = int()
for char in input_text:
    if char == "a":
        sum += a
    elif char == "e":
        sum += e
    elif char == "i":
        sum += i
    elif char == "o":
        sum += o
    elif char == "u":
        sum += u
print(sum)