n = int(input())
minimum = int()
maximum = int()

numbers = []
for i in range (0, n):
    number = int(input())
    numbers.append(number)

minimum = min(numbers)
maximum = max(numbers)

print("Max number:", maximum)
print("Min number:", minimum)