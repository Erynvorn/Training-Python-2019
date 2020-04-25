def sum_even_numbers(seq): 
    ret = 0
    if seq == []:
        return 0
    else:
        for i in range(len(seq)):
            if int(seq[i]) == seq[i] and seq[i] % 2 == 0:
                ret += seq[i]
    return ret
    pass

"""
return the sum of even number. 4 or 4.000 included.
"""
