def bubble(m):
    l=m[:]
    print(l)
    i = 0
    sol = []
    ll = len(l)
    count = ll * ll
    while count > 0 :
        while i < ll-1 :
            if l[i] > l[i+1] :
                temp = l[i+1]
                l[i+1] = l[i]
                l[i]=temp
                sol.append(l[:])
            i += 1
        i=0
        count -= 1
    #your code
    return sol
