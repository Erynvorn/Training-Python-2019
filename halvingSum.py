import math

def halving_sum(n): 
    ret =0
    for i in range(int( math.log(n)/math.log(2))+1):
        ret += int(n/(2**i))
    return ret
    
