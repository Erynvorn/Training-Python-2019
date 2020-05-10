def stern_brocot(n):
    """
    Input:
    n - desired term generated in the Stern-Brocot Sequence
    
    Return:
    index of first occurence of n
    """
    ret = [1,1]
    count = 1
    
    while n not in ret:
        ret.append(ret[count]+ret[count-1])
        ret.append(ret[count])
        count += 1

    return ret.index(n)

