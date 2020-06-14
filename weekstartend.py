from datetime import datetime

def monlen(yr, mon):
    if mon == 2 and yr %4 != 4:
        return 28 
    elif mon == 2 : 
        return 29
    if mon in (1,3,5,7,8,10,12) : 
        return 31 
    else : 
        return 30


def week_start_date(dt):
    if dt.day-dt.weekday() > 0 :
        return dt.replace( day=dt.day-dt.weekday())
    elif dt.month == 1:
        dt.replace ( year = dt.year-1 )
        dt.replace(month = 12)
        dt.replace(day= dt.day+monlen(dt.year,dt.month-1)-dt.weekday())
        return dt
    else : 
        return dt.replace( month = dt.month -1 ,day = dt.day+monlen(dt.year,dt.month-1)-dt.weekday())
        
        
    #insert code here issue for the month length can vary
    
def week_end_date(dt):
    l = monlen(dt.year,dt.month)
    if dt.day + 6- dt.weekday() <= l:
        print('normal case', dt.day + dt.weekday())
        return dt.replace(day = dt.day + 6 - dt.weekday())
    elif dt.month < 12 :
        return dt.replace(month = dt.month+1, day= -l +dt.day+ 6 - dt.weekday())
    else :
        return dt.replace(year = dt.year+1, month = 1, day=-l+dt.day+6-dt.weekday())
    return dt.replace( day = dt.day + 6 - dt.weekday())
