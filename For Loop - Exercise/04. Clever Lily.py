age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_counter = 0
money_saved = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_saved += i * 5 - 1
    else:
        toys_counter += 1

total_money = money_saved + (toys_counter * toy_price)

if total_money >= washing_machine_price:
    remaining_money = total_money - washing_machine_price
    print(f"Yes! {remaining_money:.2f}")
else:
    needed_money = washing_machine_price - total_money
    print(f"No! {needed_money:.2f}")