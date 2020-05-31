def complete_series(seq): 
    s = set(seq)
    print(s)
    if len(s) < len(seq):
        return [0]
    else: 
        return [ x for x in range(max(seq)+1)]
    # your code here
    pass

def complete_series(a):
    return list(range(max(a) + 1)) if len(a) == len(set(a)) else [0]
