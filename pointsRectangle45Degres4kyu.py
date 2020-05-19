import math

def rectangle_rotation(a, b):
    na = a // (math.sqrt(2))
    nb = b // (math.sqrt(2))
    #print(na,nb)

    if na % 2 == 0 and nb % 2 == 0:
        return (na + 1) * (nb +1) + (na * nb)
    
    elif na % 2 == 1 and nb % 2 == 1:
        return (na+1) *(nb+1) + na * nb
        
    else:  # na % 2 == 0 and nb % 2 == 1:
        return  (na) * (nb + 1) + (na+1) * (nb)


    #nombre de point coordonnees entieres dans un rectangle incline a 45 degrees
