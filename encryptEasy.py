def encrypt_this(text):
    t = text.split()
    v = []
    for i in t:
        if len(i) == 1:
            v.append(str(ord(i[0])))
        elif len(i) == 2:
            v.append(str(ord(i[0]))+ i[1])
        elif len(i) == 3:
            v.append(str(ord(i[0])) + i[2] + i[1])
        elif len(i) > 3:
            v.append(str(ord(i[0]))+i[-1]+i[2:-1]+i[1])
    return ' '.join(v)
