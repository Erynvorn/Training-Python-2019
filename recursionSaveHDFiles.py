def save(sizes, hd): 
    
    nbr = 0
    return recsave(sizes,hd,nbr)
    
def recsave(sizes, hd, nbr):
    if sizes != [] and sizes[0]-hd <= 0:
        nbr += 1
        hd -= sizes[0]
        del sizes[0]
        return recsave(sizes, hd, nbr)
    return nbr

print(save([2,3,4,5,2,7],16))
