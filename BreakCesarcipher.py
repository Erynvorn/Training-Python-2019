def break_caesar(message):
    message=message.casefold()
    for i in ['!','?','.',',','(',')',':',';'] :
        message = message.replace(i," ")
    rot=[]
    for i in range(26):
        rot.append(rotation(message,i).split())   
    common=[]
    for t in range(26):
        common.append(len(set(rot[t]) & set(WORDS)))
    res = common.index(max(common))
    return (26-res) %26
    return  # the most likely shift value as an integer
    
    
def rotation(message,index):
    decode=[]
    m=[]
    for i in message: m.append(i)
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    beta="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(m)):
        if m[i] in alpha :
            decode.append(alpha[(alpha.index(m[i])+index) % 26])
        elif m[i] in beta:
            decode.append(beta[(beta.index(m[i])+index) % 26])
        else:
            decode.append(m[i])
    return "".join(decode)
