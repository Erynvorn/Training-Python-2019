import hashlib

def password_cracker(hash):
    #one character
    alpha="abcdefghijklmnopqrstuvwxyz"
    if hashlib.sha1(b"").hexdigest() == hash : return ""
    
    for i in alpha :
        mybyte = i.encode('utf-8')
        if hashlib.sha1(mybyte).hexdigest() == hash : 
            return "test"
            
    #two characters
    for i in alpha :
        for j in alpha :
            mybyte = i.encode('utf-8')+j.encode('utf-8')
            if hashlib.sha1(mybyte).hexdigest() == hash : return i+j
            
    #three characters
    for i in alpha :
        for j in alpha :
            for k in alpha :
                mybyte = i.encode('utf-8')+j.encode('utf-8')+k.encode('utf-8')
                if hashlib.sha1(mybyte).hexdigest() == hash : return i+j+k
    
    #four characters
    for i in alpha :
        for j in alpha :
            for k in alpha :
                for l in alpha :
                    mybyte = i.encode('utf-8')+j.encode('utf-8')+k.encode('utf-8')
                    mybyte = mybyte + l.encode('utf-8')
                    if hashlib.sha1(mybyte).hexdigest() == hash : return i+j+k+l
    #five characters
    for i in alpha :
        for j in alpha :
            for k in alpha :
                for l in alpha :
                    for m in alpha :
                        mybyte = i.encode('utf-8')+j.encode('utf-8')+k.encode('utf-8')
                        mybyte = mybyte + l.encode('utf-8')+m.encode('utf-8')
                        if hashlib.sha1(mybyte).hexdigest() == hash : return i+j+k+l+m
    pass
