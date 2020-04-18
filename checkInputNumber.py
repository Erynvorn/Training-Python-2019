import math

def circleArea(r):
    try:
        int(r)
        textType = "int"
    except ValueError:
        try:
            float(r)
            textType = "float"
        except ValueError:
            textType = "string"
            
    if (textType == "int" or textType == "float") and r > 0:
        return round(math.pi*r*r,2)
    else:
        return False
    if textType == "string":
        return False
