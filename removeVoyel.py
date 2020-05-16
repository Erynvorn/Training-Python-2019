#remove all voyels

import re

def shortcut( s ):
    reg = re.compile(r'[aeiou]')
    return reg.sub('',s)
    # ...


def shortcut(s):
    return s.translate(None, 'aeiou')
