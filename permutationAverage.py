
def permutation_average(n):
    l = len(str(n))
    ret = 0
    for j in str(n):
        ret += int(j)
    return round( ret * int('1' * l) / l)
