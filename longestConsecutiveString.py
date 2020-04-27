def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0 :
        return ""
    
    ll = []
    maximus = 0
    ind = 0
    
    for i in range(len(strarr)-k+1):
        s = 0
        for j in range(k):
            s += len(strarr[i+j])
        
        if s > maximus:
            maximus = s
            ind = i

    return ''.join(strarr[ind:ind+k])
