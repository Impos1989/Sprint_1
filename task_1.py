time_data = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes_sum = 0

for time in time_data.split(','):
    for part in time.split():
        if 'h' in part:
            hours = int(part.replace('h', ''))
            minutes_sum += hours * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            minutes_sum += minutes
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            minutes_sum += seconds // 60

print(minutes_sum)