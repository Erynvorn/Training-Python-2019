#parsing a string with a regular expression

import re

def hydrate(ds): 
    num = re.compile(r'(\d)+')
    li = num.findall(ds)
    print(li)
    if li ==[]:
        return 0
    ret = 0
    for i in li:
        ret += int(i)
    if ret == 1:
        return str('1 glass of water')
    return str(str(ret) + ' glasses of water')

"""
eturn a string suggesting how many glasses of water you should drink to not be hungover.

Example parties:

Input 0:

"1 beer"

Output 0:

"1 glass of water"

Explaination 0:

You drank one standard drink

Input 1:

"1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"

Output 1:

"10 glasses of water
"""
