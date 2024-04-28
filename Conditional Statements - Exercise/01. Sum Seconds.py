import math

first_number = int(input())
second_number = int(input())
third_number = int(input())

total_time = first_number + second_number + third_number

minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')