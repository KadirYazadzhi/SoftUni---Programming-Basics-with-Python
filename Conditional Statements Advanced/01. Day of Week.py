numberOfTheDay = int(input())

if  numberOfTheDay == 1:
    day = 'Monday'
elif numberOfTheDay == 2:
    day = 'Tuesday'
elif numberOfTheDay == 3:
    day = 'Wednesday'
elif numberOfTheDay == 4:
    day = 'Thursday'
elif numberOfTheDay == 5:
    day = 'Friday'
elif numberOfTheDay == 6:
    day = 'Saturday'
elif numberOfTheDay == 7:
    day = 'Sunday'
else:
    day = 'Error'
print(day)