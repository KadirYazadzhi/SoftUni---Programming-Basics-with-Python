dayOfTheWeek = input()

if dayOfTheWeek == "Monday":
    type = 'Working day'
elif dayOfTheWeek == "Tuesday":
        type = 'Working day'
elif dayOfTheWeek == "Wednesday":
        type = 'Working day'
elif dayOfTheWeek == "Thursday":
        type = 'Working day'
elif dayOfTheWeek == "Friday":
        type = 'Working day'
elif dayOfTheWeek == "Saturday":
        type = 'Weekend'
elif dayOfTheWeek == "Sunday":
        type = 'Weekend'
else:
    type = 'Error'

print(type)