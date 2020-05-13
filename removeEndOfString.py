#remove ! at the end of a string

import re

def remove(s):
    reg = re.compile(r'(!+)$')
    ret = reg.sub('',s)
    return ret
    pass

def remove(s):
    return s.rstrip("!")
