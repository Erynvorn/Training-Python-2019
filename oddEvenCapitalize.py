def capitalize(s):
    a = ''
    b = ''
    
    for i in range(len(s)):
        a += s[i].upper()
        b += s[i]
        a,b = b,a
    
    if len(s) % 2 == 0:
        return [a,b]
    else :
        return [b,a]
    
    pass
