apartment_length = int(input())
apartment_width = int(input())
apartment_height = int(input())

total_volume = apartment_length * apartment_width * apartment_height

while True:
    command = input()
    if command == "Done":
        break
    volume_taken = int(command)
    total_volume -= volume_taken
    if total_volume <= 0:
        break

if total_volume <= 0:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")
else:
    print(f"{total_volume} Cubic meters left.")