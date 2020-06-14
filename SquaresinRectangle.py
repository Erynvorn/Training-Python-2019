def sqInRect(lng, wdth):
    if lng == wdth :return None
    else : 
        ret= []
        next(lng,wdth,ret)
        return ret 
        # your code
        
def next(l,w,ret):
    if l == w : 
        ret.append(l)
        return ret
    else :
        ret.append(min(l,w))
        next(min(l,w),max(l,w)-min(l,w),ret)
