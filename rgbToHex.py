def rgb(r, g, b):
    r = max( r, 0)
    r = min (r, 255)
    g = max( g, 0)
    g = min (g, 255)
    b = max( b, 0)
    b = min (b, 255)
    rh = hex(r)
    gh = hex(g)
    bh = hex(b)
    
    if len(rh) == 3:
        rhex = '0'+rh[2].upper()
    else:
        rhex = rh[2:].upper()
        
    if len(gh) == 3:
        ghex = '0'+gh[2].upper()
    else:
        ghex = gh[2:].upper()
        
    if len(bh) == 3:
        bhex = '0'+bh[2].upper()
    else:
        bhex = bh[2:].upper()
        
    return rhex+ghex+bhex
