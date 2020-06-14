def rot13(message):
    decode=[]
    m=[]
    for i in message: m.append(i)
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(m)):
        if m[i] in alpha : 
            decode.append(alpha[(alpha.index(m[i])+13) % 26])
        elif m[i] in beta: 
            decode.append(beta[(beta.index(m[i])+13) % 26])
        else:
            decode.append(m[i])
    return "".join(decode)
