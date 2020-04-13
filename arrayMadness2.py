def array_madness(a,b):
    print(a)
    print(b)
    aa = 0
    bb = 0
    for i in range(len(a)):
        aa += a[i]**2
    for j in range(len(b)):
        bb += b[j]**3
    if aa > bb:
        return True
    return False
    # Ready, get, set, GO!!!
