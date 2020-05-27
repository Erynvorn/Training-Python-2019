def josephus_survivor(n,k):
    items = list(range(1,n+1))

    curr = (k-1) % len(items)
    
    while len(items) > 1:      
        del items[curr]
        curr = (curr + k - 1 ) % (len(items))
        
    return items[0]

def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1
