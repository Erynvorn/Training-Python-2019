def testit(s):
    print(s)
    ret =[]
    if len(s) == 0 :
        return ""
    elif len(s) == 1 :
        return s
    else: 
        # if len(s) even 
        if len(s) % 2 == 0:
            for i in range(int(len(s)/2)) :
                if ord(s[2*i]) == ord(s[2*i+1]):
                    ret.append(s[2*i])
                elif ord(s[2*i]) + 1 == ord(s[2*i+1]):
                    ret.append(s[2*i])
                else:
                    ret.append(chr(int((ord(s[2*i])+ord(s[2*i+1]))/2)))
        else :
            for i in range(int((len(s)-1)/2)) :
                if ord(s[2*i]) == ord(s[2*i+1]):
                    ret.append(s[2*i])
                elif ord(s[2*i]) + 1 == ord(s[2*i+1]):
                    ret.append(s[2*i])
                else:
                    ret.append(chr(int((ord(s[2*i])+ord(s[2*i+1]))/2)))
            ret.append(s[len(s)-1])        
    return ''.join(ret)
   
     
