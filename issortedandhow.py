def is_sorted_and_how(a):
    arr=a[:]
    arr.sort()
    print(a, arr)
    if arr == a[:] : 
        return "yes, ascending"
    arr.sort(reverse=True)
    if arr == a[:] :
        return "yes, descending"
    return "no"
