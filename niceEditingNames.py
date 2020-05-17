def namelist(names):
    ret = []
    
    if len(names) == 0:
        return ''
    for i in range(len(names)):
        for j in names[i].values():
            ret.append(j)
    if len(ret) == 1:
        return ''.join(ret)
    elif len(ret) == 2:
        return ' & '.join(ret)
    else:
        return ', '.join(ret[:-1]) + ' & ' + ret[-1]

# nice editing string
