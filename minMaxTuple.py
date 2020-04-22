def get_min_max(seq): 
    
    min = seq[0]
    max = seq[0]
    for i in range(len(seq)):
        if seq[i] < min:    
            min = seq[i]
        if seq[i] > max:
            max = seq[i]
    return (min, max)
    pass

"""
get min max and return a tuple
