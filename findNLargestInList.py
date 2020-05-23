ef largest(n,xs):
    x = max(xs)
    print(x)
    ret =[]
    for i in range(n):
        ret.insert(0,max(xs))
        xs.remove(max(xs))
    return ret
    """Find the n highest elements in a list"""
    
def largest(n, xs):
  "Find the n highest elements in a list"
  
  return sorted(xs)[-n:];
