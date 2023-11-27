def convert_to_24_hour(hour, minute, period):
    if period == 'am':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f"{hour:02d}{minute:02d}"

hour = 8
minute = 30
period = 'am'

result = convert_to_24_hour(hour,minute,period)
print(f" 24-hour format is: {result}")