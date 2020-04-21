def remove_duplicate_words(s):
    ff = s.split()
    sol =[]
    sol.append(ff[0])
    for i in ff:
        if i not in sol:
            sol.append(i)
    return ' '.join(sol)
    pass

"""
import re

def remove_duplicate_words(s):
    p = re.compile(r'(\b\w+\b)(.*)\s\1')
    t = p.sub(r'\1\2',s)
    if t == s:
        return s
    return remove_duplicate_words(t)



Using a dictionary:

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))

"""
