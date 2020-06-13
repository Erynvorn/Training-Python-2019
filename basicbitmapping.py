def to_bits(string):
    ll = string.split("\n")
    sol=[]
    i=0
    while i < 5000 :
        sol.append(0)
        i += 1
    for i in ll :
        sol[int(i)] = 1
    return sol



def to_bits(s):
    lst = [0] * 5000
    for i in map(int,s.split()): lst[i] = 1
    return lst
