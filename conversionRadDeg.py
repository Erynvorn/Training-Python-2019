def degrees(rad):
    ret = round(rad *180 / math.pi , 2)
    if int(ret) == ret:   
        ret = int(ret)
    
    return str(ret)+'deg'
    #your code here

def radians(deg):
    ret =  round(deg *math.pi / 180 , 2)
    if int(ret) == ret:
        ret= int(ret)
    return str(ret)+'rad'

def degrees(rad):
    return '%gdeg' % round(180 * rad / math.pi, 2)

def radians(deg):
    return '%grad' % round(math.pi * deg / 180, 2)
