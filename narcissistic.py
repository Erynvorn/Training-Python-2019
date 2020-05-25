def narcissistic( value ):
    n = [int(x) for x in str(value)]
    ret = 0
    l = len(n)
  
    for i in range(l):
        ret += n[i]**(l)
        
    return value == ret

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
