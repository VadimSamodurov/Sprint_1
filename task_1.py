time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

time_values = time_string.split(',')

for time_value in time_values:

    time_value = time_value.strip()

    parts = time_value.split()

    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            total_minutes += minutes
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)