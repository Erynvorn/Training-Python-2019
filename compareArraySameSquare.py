def comp(array1, array2):
    if array1 == None and array2 == []:
        return False
    if array2 == None and array1 ==[]:
        return False
    if array1 == [] and array2 != []:
        return False
    print(array1, array2)
    for i in range(len(array1)):
        if array1[i]**2 not in array2:
            return False
        else:
            array2.remove(array1[i]**2)
    return True
    # your code


def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
