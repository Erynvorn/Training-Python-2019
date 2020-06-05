def longest(s1, s2):
    s=s1+s2
    ret = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i in s:    
            ret.append(i)
    return ''.join(ret)
    
    # your code
    
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
