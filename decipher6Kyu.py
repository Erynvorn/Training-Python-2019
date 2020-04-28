import re
digit = re.compile(r'^[0-9]*')

def decipher_this(string):
    ret = []
    d = string.split()
    for i in d:
        cc = digit.search(i).group()
        j = digit.sub('',i)
        i = chr(int(cc))+ j
        l = len (i)
        if l > 2: 
            a = i[len(i)-1]
            b = i[1]
            j = i[0]+a+i[2:len(i)-1]+b
            i = j 
            ret.append(i)
        else:
            ret.append(i)
            
    return ' '.join(ret)

"""
used RE to select the digits

"""
