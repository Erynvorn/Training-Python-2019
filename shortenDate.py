#remove end of line after the comma

def shorten_to_date(long_date):
    return long_date[:long_date.index(',')]
    #your code here

def shorten_to_date(long_date):
    return long_date.split(',')[0]
