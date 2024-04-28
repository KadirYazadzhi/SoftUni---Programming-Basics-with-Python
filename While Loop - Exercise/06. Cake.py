width = int(input())
length = int(input())

total_pieces = width * length
taken_pieces = 0

while True:
    command = input()
    if command == "STOP":
        break
    taken_pieces += int(command)

    if taken_pieces >= total_pieces:
        print(f"No more cake left! You need {taken_pieces - total_pieces} pieces more.")
        break

if taken_pieces < total_pieces:
    print(f"{total_pieces - taken_pieces} pieces are left.")