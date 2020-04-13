def array_madness(a,b):
    aa = 0
    bb = 0
    for i in range(len(a)):
        aa += a[i]**2
        bb += b[i]**3
    if aa > bb:
        return True
    return False
    # Ready, get, set, GO!!!
