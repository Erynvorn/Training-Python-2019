def sc(s):
    t=[]
    s1=[]
    for i in s : s1.append(i)
    u=s.casefold()
    for i in u: t.append(i)
    sup=[]
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l=len(alphabet)
    for i in range(l):
        if t.count(alphabet[i]) == 1:
            sup.append(i)
    for j in sup :
        s1[t.index(alphabet[j])]=" "
    return "".join(s1).replace(" ","")
