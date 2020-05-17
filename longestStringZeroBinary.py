import re

def gap(num):
    b = bin(num)
    print(b)
    reg = re.compile(r'(0+1)')
    ret = reg.findall(b)
    print(ret)
    if ret == [] :
        return 0
    
    max =0
    for i in range(len(ret)):
        if len(ret[i]) > max:
            max = len(ret[i])
    return max -1
    #//code me

"""
Find the longest set of zero in a binary number )b1000010001000100 finsihing by 1
