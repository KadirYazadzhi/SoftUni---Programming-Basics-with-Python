exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_minutes = exam_hour * 60 + exam_minute
arrival_time_minutes = arrival_hour * 60 + arrival_minute

difference = arrival_time_minutes - exam_time_minutes

if difference > 0:
    print("Late")
elif difference >= -30:
    print("On time")
else:
    print("Early")

absolute_difference = abs(difference)

hours = absolute_difference // 60
minutes = absolute_difference % 60

if absolute_difference >= 60:
    print(f"{hours}:{minutes:02d} hours {'before' if difference < 0 else 'after'} the start")
else:
    print(f"{minutes} minutes {'before' if difference < 0 else 'after'} the start")