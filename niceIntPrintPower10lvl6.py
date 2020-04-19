#level 6 print nicely integer with 10 powers

def simplify(n): 
    if n == 0:
        return ''
    ret = ''
    p = 0
    while True:
        if n == 0:     # n = 0 ou fin du traitement
            if ret[-1]=='+':
                ret = ret[0:-1]
            return ret 
            break
        if p == 0:     # first digit
            if n % 10 != 0:
                ret += str(n%10)
            n = ( n - n % 10 ) / 10
            p += 1
        if n % 10 == 0:  # multiple of 10
            n = n / 10
            p += 1
        else:
            ret = str( int(n% 10))+'*'+str(10**p)+'+'+ ret
            n = ( n - n % 10 ) / 10    # si fini on le triate avec le premier test 
            p += 1
    # return ret

print(simplify(5643))

# result is 5*1000+6*100+4*10+3  NICE

"""
Given a positive integer as input, return the output as a string in the following format:

Each element, corresponding to a digit of the number, multiplied by a power of 10 in such a way that with the sum of these elements you can obtain the original number.

Examples

Input	Output
0	""
56	"5*10+6"
60	"6*10"
999	"9*100+9*10+9"
10004	"1*10000+4"
Note: input >= 0
"""
