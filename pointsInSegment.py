def segments(m, a):
    ret=[]
    i = 0
    if a == []:
        while i <= m:
            ret.append(i)
            i += 1
    else:
        i = 0
        while i <= m:
            q = False
            for j in a:
                if i < j[0] or i> j[1]:
                    q = True
                else:
                    q = False
                    break
            if q == True:
                ret.append(i)
            i += 1 
        
    return ret
