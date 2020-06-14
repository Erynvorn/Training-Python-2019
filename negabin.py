def negabin(i,ret):
    div = 0
    rest = 0
    if i == 0 : return ret
    else: 
        div = round(i/(-2))
        rest = i+2*div
        if rest < 0 : 
            rest +=2
            div += 1
        print(div,rest)
        ret = str(rest) + ret
        return negabin(div,ret)


def int_to_negabinary(i):
    res = negabin(i,'')
    if res == '' : return '0'
    else: 
        return res


def negabinary_to_int(s):
    res = 0
    for i in range(len(s)-1) :
        #print('len ' , len(s) , 'i  ', i)
        res += (-2 *int(s[i])) ** (len(s) - i-1) 
        
        print('len ' , len(s) , 'i  ', i, 'res ' ,res)
    return res+int(s[len(s)-1])
    
