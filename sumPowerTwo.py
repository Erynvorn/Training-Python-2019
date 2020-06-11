import math
# return an array of numbers (that are a power of 2)
# for which the input "n" is the sum
def powers(n):
    ret = []
    co = 0
    while True:
        print(n)
        if n == 0:
            return ret
        co = math.floor(math.log(n)/math.log(2)) 
        
        n -= 2**co
        if n == -1:    
            co -= 1
            n = -1 + 2**(co+1) -2**co
        
        ret.insert(0,2**co)
            
        print(co, n)
    return ret



def powers(n):
    return [1<<i for i, x in enumerate(reversed(bin(n))) if x == "1"]



def powers(n):
    s = bin(n)[::-1]
    return [2**i for i, x in enumerate(s) if x == '1']
