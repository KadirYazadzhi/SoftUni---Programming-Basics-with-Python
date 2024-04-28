town = input()
salary = float(input())


if town == "Sofia":
    if 0 <= salary <= 500:
        print("{:.2f}".format(salary * 0.05))
    elif 500 < salary <= 1000:
        print("{:.2f}".format(salary * 0.07))
    elif 1000 < salary <= 10000:
        print("{:.2f}".format(salary * 0.08))
    elif salary > 10000:
        print("{:.2f}".format(salary * 0.12))
    else:
        print("error")

elif town == "Varna":
    if 0 <= salary <= 500:
        print("{:.2f}".format(salary * 0.045))
    elif 500 < salary <= 1000:
        print("{:.2f}".format(salary * 0.075))
    elif 1000 < salary <= 10000:
        print("{:.2f}".format(salary * 0.1))
    elif salary > 10000:
        print("{:.2f}".format(salary * 0.13))
    else:
        print("error")

elif town == "Plovdiv":
    if 0 <= salary <= 500:
        print("{:.2f}".format(salary * 0.055))
    elif 500 < salary <= 1000:
        print("{:.2f}".format(salary * 0.08))
    elif 1000 < salary <= 10000:
        print("{:.2f}".format(salary * 0.12))
    elif salary > 10000:
        print("{:.2f}".format(salary * 0.145))
    else:
        print("error")
else:
    print("error")