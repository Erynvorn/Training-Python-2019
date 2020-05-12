def uniq(seq): 

    if seq == []:
        return []
    if len(seq) == 1:
        return seq
        
    ret = []
    ret.append(seq[0])
    
    for i in range(1,len(seq)):
        if seq[i] != seq[i-1]:
            ret.append(seq[i])
            
    return ret


def uniq(seq): 
    return [k for k,_ in groupby(seq)]
