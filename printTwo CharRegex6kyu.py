import re

def solution(s):
    if len(s) % 2 == 1 :
        s += '_'
    reg = re.compile(r'\w{2}')
    return reg.findall(s)
    pass


def solution(s):
    return re.findall(".{2}", s + "_")

