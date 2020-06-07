def any_odd(x):
    print(x)
    if x == 2 : 
        return 1
    elif x == 0 or x == 1:
        return 0
    y = str(f"{x:b}")
    print(y)
    for i in range(len(y)-2,-1,-2):
        print(i, y[i])
        if y[i] == '1':    
            return 1
    return 0
    # Write code here...


def any_odd(x):
    return x & 0xaaaaaaaa != 0
