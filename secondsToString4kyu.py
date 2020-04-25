def format_duration(seconds):    #super basic approach No use of time functions
    if seconds == 0:
        return 'now'
    min = 60
    hour = 60 * min
    day = 24 * hour
    year = 365 * day
    ret = []
     
    y = seconds // year
    d = (seconds - y * year) // day
    h = (seconds - y * year - d * day) // hour
    m = (seconds - y * year - d * day - h * hour) // min
    s = (seconds - y * year - d * day - h * hour - m * min)
    print(str(y)+' years '+str(d)+ ' days '+ str(h) + ' hours '+ str(m) + 'minutes' +str (s)+'seconds')
    
    if s  != 0 : #and y+d+h+m == 0:
        if s == 1:
            ret.append('1 second')
        else:
            ret.append(str(s)+' seconds')
        
    if m != 0 :
        if m == 1:
            ret.insert(0,'1 minute')
        else:
            ret.insert(0,str(m)+' minutes')
        
    if h != 0 :
        if h == 1:
            ret.insert(0,'1 hour')
        else:
            ret.insert(0,str(h)+' hours')
        
    if d != 0 :
        if d == 1:
            ret.insert(0,'1 day')
        else:
            ret.insert(0,str(d)+' days')
    
    if y != 0 :
        if y == 1:
            ret.insert(0,'1 year')
        else:
            ret.insert(0,str(y)+' years')
      
    if len(ret) == 1:
        return ret[0]
    elif len(ret) == 2:
        return ret[0]+' and '+ret[1]
    elif len(ret) == 3:
        return ret[0]+', '+ret[1]+' and '+ret[2]
    elif len(ret) == 4:
        return ret[0]+', '+ret[1]+', '+ret[2]+' and '+ret[3]
    else:
        return ret[0]+', '+ret[1]+', '+ret[2]+', '+ret[3]+' and '+ret[4]
  
