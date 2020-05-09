import re

def rake_garden(garden):
    g = garden.split()
    ret = []
    for i in range(len(g)):
        if g[i] != 'gravel' and g[i] != 'rock':
            ret.append( 'gravel' )
        else:
            ret.append(g[i])
    return ' '.join(ret)
    pass

