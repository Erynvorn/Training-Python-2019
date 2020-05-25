def max_sequence(arr):
    print(arr)
    if arr == [] or max(arr) <= 0:
        return 0
    if min(arr) >= 0:
        return sum(arr)
    m = 0
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            m = max (m, sum(arr[i:j]))
            
    return m        
    # ... 

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max
