data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

output = []

def parsing_duration(duration) :
    parts = duration.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    return weeks, days, hours, minutes

def converter(weeks) :
    def days(days) :
        def hours(hours) :
            def minutes(minutes) :
                return ((((weeks * 7)+ days)* 24+ hours)* 60)+minutes
            return minutes
        return hours
    return days

for duration in data:
    weeks, days, hours, minutes = parsing_duration(duration)
    total_minutes = converter (weeks)(days)(hours)(minutes)
    output.append(total_minutes)

print(f"Output = {output}")