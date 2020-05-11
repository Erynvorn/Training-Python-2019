# invert the triangle
# maketri(size_of_triangle) can be called for convenience

def invert_triangle(t):
    ret = []
    for i in range(len(t)):
        if t[i] == " ":
            ret.insert(0,"#")
        elif t[i] == "#":
            ret.insert(0," ")
        else:
            ret.insert(0,t[i])
    return ''.join(ret)

# Invert triange

def invert_triangle(t):
    return t[::-1].translate(str.maketrans('# ', ' #'))
