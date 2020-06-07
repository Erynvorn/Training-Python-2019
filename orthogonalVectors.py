def is_orthogonal(u, v): 
    ret = 0
    for i in range(len(u)):
        ret += u[i]*v[i]
    return ret == 0
    pass


def is_orthogonal(u, v): 
    return sum(i*j for i,j in zip(u,v)) == 0

is_orthogonal = lambda u, v: not sum(a * b for a, b in zip(u, v))
