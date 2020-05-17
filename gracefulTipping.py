import math

def graceful_tipping(bill):
    b = bill *1.15
    if b < 10:
        return round(b+0.5)
    l = math.floor((math.log(b)/math.log(10)))
    r = b % 10**(l)
    if r < 10**(l)/2:
        new = 10**(l)/2
    else:
        new = 10**l
    return int((b-r+new))

# Graceful tipping
