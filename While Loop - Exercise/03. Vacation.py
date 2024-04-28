required_money = float(input())
current_money = float(input())

consecutive_days = 0
total_days = 0

while current_money < required_money and consecutive_days < 5:
    action = input()
    amount = float(input())
    total_days += 1

    if action == "spend":
        current_money -= amount
        if current_money < 0:
            current_money = 0
        consecutive_days += 1
    elif action == "save":
        current_money += amount
        consecutive_days = 0

if current_money >= required_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
