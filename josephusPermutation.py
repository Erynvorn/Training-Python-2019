def josephus(items,k):
    if items == []:
        return []
    print(items,k)
    curr = (k-1) % len(items)
    ret = []
    while len(items) > 1:
        ret.append(items[curr])
        del items[curr]
        print('curr ', curr, ' k ', k, 'len ' , len(items))
        print(ret)
        curr = (curr + k - 1 ) % (len(items))

    ret = ret + items
    return ret

def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys
