#difference of cuboid volumes

def find_difference(a, b):
    vola, volb = 1 , 1
    for i in range(3):
        vola *= a[i]
        volb *= b[i]
    return abs(vola-volb)

