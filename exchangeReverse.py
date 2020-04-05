def exchange_with(a, b):
    a.reverse()
    b.reverse()

    temp = []
    temp.extend(a)
    
    a.clear()
    a.extend(b)
    
    b.clear()
    b.extend(temp)
    return
