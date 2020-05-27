def solution(n,d):
    if d<=0:
        return []
    a = n % 10**d
    ret  = [int(digit) for digit in str(a)]
    while len(ret) < d and n > 10**d :
        print(len(ret),d)
        ret.insert(0, 0)
    return ret
    pass

def solution(n, d):
    return [int(c) for c in str(n)[-d:]] if d > 0 else []
