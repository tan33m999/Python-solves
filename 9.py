def getHoursMinutesSeconds(totalSeconds):
    x = totalSeconds
    hour = x // 3600
    mins = (x - (hour * 3600)) // 60
    sec = x - (hour * 3600) - (mins * 60)
    time = []
    if hour > 0:
        time.append(str(hour) + 'h')
    else: pass
    if mins > 0:
        time.append(str(mins) + 'm')
    else: pass
    if sec > 0:
        time.append(str(sec) + 's')
    elif hour == 0 and mins == 0:
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
