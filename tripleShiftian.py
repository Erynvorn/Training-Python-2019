def triple_shiftian(base,n):
    tot=[base[0],base[1],base[2],0]
    
    for i  in range(n):
        if n == 0 :
            return 3
        if n < 3 :
            return base[n]
        else: 
            tot[3] = 4 * tot[2] -5 * tot[1] + 3*tot[0]
            tot[0] = tot[1]
            tot[1] = tot[2]
            tot[2] = tot[3]
            
    return tot[0]
 
def triple_shiftian(base,n):
    a, b, c = base
    for _ in xrange(n):
        a, b, c = b, c, 4*c - 5*b + 3*a
    
    return a
