def add_time(start, duration, starting_day=''):
    parts = start.split()
    time = parts[0].split(':')
    end = parts[1]

    if end == 'PM':
        hour = int(time[0]) + 12
        time[0] = str(hour)

    dur = duration.split(':')

    new_hr = int(time[0]) + int(dur[0])
    new_min = int(time[1]) + int(dur[1])

    if new_min >= 60:
        hr_add = new_min // 60
        new_min %= 60
        new_hr += hr_add
    
    days_add = 0
    if new_hr > 24:
        days_add = new_hr // 24
        new_hr %= 24
    
    if new_hr > 0 and new_hr < 12:
        end = 'AM'
    elif new_hr == 12:
        end = 'PM'
    elif new_hr > 12:
        end = 'PM'
        new_hr -= 12
    else:
        end = 'AM'
        new_hr += 12

    if days_add > 0:
        if days_add == 1:
            days_later = ' (next day)'
        else:
            days_later = ' (' + str(days_add) + ' days later)'
    else:
        days_later = ''

    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    if starting_day:
        weeks = days_add // 7
        y = weekdays.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
        if y > 6:
            y -= 7
        day = ', ' + weekdays[y]
    else:
        day = ''

    new_time = str(new_hr) + ':' + \
        (str(new_min) if new_min > 9 else ('0' + str(new_min))) + \
            ' ' + end + day + days_later

    return new_time