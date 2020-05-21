# color and code Colors

def yellow_be_gone(cnc):
    y = ['gold','khaki', 'lemonchiffon', 'lightgoldenrodyellow', 'lightyellow', 'palegoldenrod', 'yellow']
    g = ['ForestGreen', 'LimeGreen' , 'PaleGreen', 'SpringGreen' , 'MintCream' , 'LightGreen', 'Lime' ]
    if cnc.lower() in y:
        return g[y.index(cnc.lower())]
    elif cnc[0]== '#':
        a,b,c = cnc[1:3], cnc[3:5] , cnc[5:]
        
        R = int(a,16)
        G = int(b,16)
        B = int(c,16)
        
        if R > B and G > B:
            if R > G :
                a,b,c = c,a,b
            else :
                a,b,c = c,b,a
            
        return '#'+ a + b + c
        
    return cnc

