from datetime import date

def most_frequent_days(year):
    print(year)
    d = date(year, 1, 1).weekday()
    wd = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday', 'Monday']
    if year % 4 == 0:
        if d == 6: 
            return [wd[0],wd[6]]
        else: 
            return [wd[d],wd[d+1]]
    else:
        return [wd[d]]

from datetime import datetime 
from calendar import day_name


def most_frequent_days(year):
    first = set(range(datetime(year, 1, 1).weekday(), 7))
    last = set(range(datetime(year, 12, 31).isoweekday()))
    return [day_name[day] for day in sorted((first & last) or (first | last))]
