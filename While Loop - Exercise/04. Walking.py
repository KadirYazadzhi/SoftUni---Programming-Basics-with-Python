goal = 10000
total_steps = 0

while total_steps < goal:
    command = input()

    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        steps_short = goal - total_steps
        if total_steps < goal:
            print(f"{steps_short} more steps to reach goal.")
        break

    steps = int(command)
    total_steps += steps

if total_steps >= goal:
    steps_over = total_steps - goal
    print("Goal reached! Good job!")
    print(f"{steps_over} steps over the goal!")