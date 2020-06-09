import string

def is_pangram(s):
    s = s.lower()
    count = {}
    for i in s:
        count.setdefault(i,0)
        count[i] = count[i]+1
    alpha='abcdefghijklmnopqrstuvwxyz'
    try:
        for i in alpha:    
            if count[i]>=1:
                pass
        return True
    except:
        return False
        
