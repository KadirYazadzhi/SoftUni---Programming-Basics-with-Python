tournaments = int(input())
starting_points = int(input())

winner = 0
final = 0
semifinal = 0
points_win = 2000
points_final = 1200
points_semif = 720

for i in range(tournaments):
    finished_position = input()
    if finished_position == "W":
        winner += 1
    elif finished_position == "F":
        final += 1
    elif finished_position == "SF":
        semifinal += 1
    else:
        pass

earned_points = winner * points_win + final * points_final + semifinal * points_semif

final_points = earned_points + starting_points
average_points = earned_points / tournaments

percent_wins = winner / tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {int(average_points)}')
print(f'{percent_wins:.2f}%')