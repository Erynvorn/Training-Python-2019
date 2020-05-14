import math

def zeros(n):
    cinq = 0
    i = 5
    if n == 0:
        return 0
    while True:
        if n/i >= 1 :
            cinq += math.floor(n/i)
            i *= 5
        else:
            break
    return cinq

"""
Number of zeros at the end of a factorial
"""
