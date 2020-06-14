def pattern(n):
    ret =[]
    r = ''
    if n<1:
        return ""
    for i in range(1,n):
        for j in range(1,i+1):
            r = r + str(i)
        r = r +'\n'
    for j in range(n):
        r = r + str(n)
    return r
