def next_happy_year(year):
    year += 1
    while True:
        y = str(year)
        if y[0] == y[1] or y[0] == y[2] or y[0] == y[3] or y[1] == y[2] or y[1] == y[3] or y[2] == y[3]:
            year += 1
        else: 
            return year
    #your code here

def next_happy_year(year):
    year += 1
    
    while len(set(str(year))) != 4:
        year += 1
    
    return year
