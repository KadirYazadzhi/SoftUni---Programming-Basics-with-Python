age = float(input())
pol = input()

if age >= 16 and pol == 'm':
    print("Mr.")
elif age < 16 and pol == 'm':
    print("Master")
elif age >= 16 and pol == 'f':
    print("Ms.")
elif age < 16 and pol == 'f':
    print("Miss")