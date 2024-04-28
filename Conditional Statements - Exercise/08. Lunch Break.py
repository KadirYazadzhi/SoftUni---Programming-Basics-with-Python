from math import ceil

name_series = input()
duration_episode = int(input())
duration_rest = int(input())

lunch_time = duration_rest / 8
rest_time = duration_rest / 4

time_left = duration_rest - lunch_time - rest_time

time_needed = time_left - duration_episode
needed_time = duration_episode - time_left

if time_left >= duration_episode:
    print(f"You have enough time to watch {name_series} and left with {ceil(time_needed)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_series}, you need {ceil(needed_time)} more minutes.")
