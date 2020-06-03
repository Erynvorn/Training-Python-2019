def smallest(n):
    p = [int(digit) for digit in str(n)]
    m = min(p)
    i = p.index(m)
    z = len(p) - p[::-1].index(m) - 1
    print(p,m, i,z)
    
    if m == 0 :
        del p[z]
        p =[str(i) for i in p] 
        if i == 1:
            return [int("".join(p)),0,i]
        return [int("".join(p)),i,0]
        
    else:
        
    while m < 10
        if z == 0 : 
            m += 1
            i = p.index(m)
            z = len(p) - p[::-1].index(m) -1
        else:
            del p[z]
            for j in range(z):
                if p[j] >= m:
                    p.insert(j,m)
                    p =[str(i) for i in p]
                    return [int("".join(p)),z,j]
        
    """
    for k in range(10):
        if k in p and k == 0:
            i = p.index(k)
            
            p.remove(0)
            
            p =[str(i) for i in p] 
            if i == 1:
                return [int("".join(p)),0,i]
            ret = [int("".join(p)),i,0]
            return ret
        elif k in p and p.index(k) == 0:
            continue
        elif k in p and p.index(k) != 0:
            i = p.index(k)
            for l in range(i):
                if k < p[l]:
                    p.remove(k)
                    p.insert(l,k)
                    print(p)
                    p =[str(i) for i in p]
                    print("".join(p))
                    return [int("".join(p)),i,l]
    # your code """
