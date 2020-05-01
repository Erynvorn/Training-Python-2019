import re

def lowercase_count(strng):
    print(strng)
    reg = re.compile(r'[a-z]')
    ret = reg.findall(strng)
    return len(ret)
