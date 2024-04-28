hours = int(input())
day = input()

if hours >= 10 and hours <= 18:
    if day == "Monday":
        print("open")
    elif day == "Tuesday":
        print("open")
    elif day == "Wednesday":
        print("open")
    elif day == "Thursday":
        print("open")
    elif day == "Friday":
        print("open")
    elif day == "Saturday":
        print("open")
    elif day == "Sunday":
        print("closed")
else:
    print("closed")