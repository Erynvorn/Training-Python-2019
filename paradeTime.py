import math

def parade_time(groups, location, speed, pref):
    ret =[]
    i = 0
    while i < len(groups):
        if pref == groups[i]:
            time = math.floor( ( location + i +1 ) / speed)
            ret.append(time)
        i += 1
    return ret


def parade_time(groups, location, speed, pref):
    return [(location+i+1) / speed for i, g in enumerate(groups) if g == pref]
