def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return "0s"
    x = totalSeconds
    hour = 0
    while x >= 3600:
        hour += 1
        x -= 3600
    mins = 0
    while x >= 60:
        mins += 1
        x -= 60
    sec = x
    time = []
    if hour > 0:
        time.append(str(hour) + 'h')
    else: pass
    if mins > 0:
        time.append(str(mins) + 'm')
    else: pass
    if sec > 0:
        time.append(str(sec) + 's')
    return " ".join(time)
assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
