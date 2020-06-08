def or_arrays(arr1, arr2, x = 0):
    ret = []
    if len(arr1) == len(arr2) :
        for i in range(len(arr1)):
            ret.append(arr1[i] | arr2[i])
        return ret
    if len(arr1) > len(arr2) :
        for i in range(len(arr2)):
            ret.append(arr1[i] | arr2[i] )
        for j in range(len(arr2), len(arr1)):
            ret.append(arr1[j] | x)
        return ret
        
    if len(arr1) < len(arr2) :
        for i in range(len(arr1)):
            ret.append(arr1[i] | arr2[i] )
        for j in range(len(arr1),len(arr2)):
            ret.append(arr2[j] |x)
        return ret


from itertools import zip_longest

def or_arrays(a1, a2, d=0):
    return [x|y for x,y in zip_longest(a1, a2, fillvalue=d)]

    
