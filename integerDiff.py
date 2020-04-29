def int_diff(arr, n):
    print(arr)
    print(n)
    count = {}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            d = abs(arr[i]-arr[j])
            count.setdefault(d , 0)
            count[d] = count[d] + 1
    ret = 0
    print(count)
    for k,v in count.items():
        if k == n:
            ret = v
    
    return ret
