product = input()
dayOfWeek = input()
broi = float(input())

banana = 2.50
apple = 1.20
orange = 0.85
grapefruit = 1.45
kiwi = 2.70
pineapple = 5.50
grapes = 3.85

bananaWeekend = 2.70
appleWeekend = 1.25
orangeWeekend = 0.90
grapefruitWeekend = 1.60
kiwiWeekend = 3.00
pineappleWeekend = 5.60
grapesWeekend = 4.20

if dayOfWeek == "Monday" or dayOfWeek == "Tuesday" or dayOfWeek == "Wednesday" or dayOfWeek == "Thursday" or dayOfWeek == "Friday":
    if product == "banana":
        print("{:.2f}".format(banana * broi))
    elif product == "apple":
        print("{:.2f}".format(apple * broi))
    elif product == "orange":
        print("{:.2f}".format(orange * broi))
    elif product == "grapefruit":
        print("{:.2f}".format(grapefruit * broi))
    elif product == "kiwi":
        print("{:.2f}".format(kiwi * broi))
    elif product == "pineapple":
        print("{:.2f}".format(pineapple * broi))
    elif product == "grapes":
        print("{:.2f}".format(grapes * broi))
    else:
        print("error")

elif dayOfWeek == "Saturday" or dayOfWeek == "Sunday":
    if product == "banana":
        print("{:.2f}".format(bananaWeekend * broi))
    elif product == "apple":
        print("{:.2f}".format(appleWeekend * broi))
    elif product == "orange":
        print("{:.2f}".format(orangeWeekend * broi))
    elif product == "grapefruit":
        print("{:.2f}".format(grapefruitWeekend * broi))
    elif product == "kiwi":
        print("{:.2f}".format(kiwiWeekend * broi))
    elif product == "pineapple":
        print("{:.2f}".format(pineappleWeekend * broi))
    elif product == "grapes":
        print("{:.2f}".format(grapesWeekend * broi))
    else:
        print("error")

else:
    print("error")