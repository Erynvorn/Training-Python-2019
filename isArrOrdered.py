def in_asc_order(arr):
    b = tuple(arr)
    arr.sort()
    c = tuple(arr)
    if b == c:
        return True
    else:
        return False
    # random_ is not allowed
    #return bool #(True or false)
    
