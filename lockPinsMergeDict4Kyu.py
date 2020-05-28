def merge(s,t):     # merge two stepss
    ret = []
    for i in range(len(s)):
        for j in range(len(t)):
            ret.append(s[i]+t[j])
    return ret

# first creating a dictonary with all options

def get_pins(observed):
    sol = { '0' : ['0','8'] , '1' : ['1','2','4'] , '2' : ['1','2','3','5'] , 
    '3' : ['2','3','6'] , '4': ['1','4','5','7'], '5': ['2','4','5','6','8'], 
    '6' : ['3','5','6','9'] , '7': ['4','7','8'] , '8': ['0','5','7','8','9'], 
    '9': ['6','8','9'], '0' :['0','8']}     
    if len(observed) == 1:
        for k,v in sol.items():
            if k == observed :
                return v
    else:
        ans = []
        for i in range(len(observed)):
            ans.append(sol[observed[i]])   #expanding to all solution
        for i in range(1,len(ans)):
            ans[0] = merge(ans[0],ans[i])   # creating all potential output
        return ans[0]


"""
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
    """
