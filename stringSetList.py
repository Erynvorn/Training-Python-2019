def in_array(array1, array2):
    print(array1, array2)
    ret = set()
    for i in array1:
        for j in array2:
            if i in j :
                ret.add(i)
                break
    ret = list(ret)
    ret.sort()
    return ret

# str in str , set and list
