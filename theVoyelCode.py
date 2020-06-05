def encode(st):
    l = []
    dict = { 'a':'1','e':'2', 'i':'3', 'o':'4', 'u':'5'}
    
    for i in range(len(st)):
        l.append(st[i])
        
    for i in range(len(st)):
        if l[i] in dict:
            l[i] = dict[l[i]]
    
    return ''.join(l) 
    
def decode(st):
    l = []
    dict = { '1':'a','2':'e','3': 'i','4': 'o','5':'u'}
    for i in range(len(st)):
        l.append(st[i])
        
    for i in range(len(st)):
        if l[i] in dict:
            l[i] = dict[l[i]]
    
    return ''.join(l) 
    


def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
