def check1800(s):
    #print(WORDS)# Your code here!
    print(s)
    a=s[6:9]
    if s[10] == '-' : 
        b = s[6:10]
        c= s[9]+s[-3:]
    else :
        b = s[6:9]+s[10]
        c = s[-4:]
    d = s[-3:]
    #print(a,b,c,d) #all possible 3 and 4 words combinations to test
    e = [a,b,c,d]
    f = []
    for i in e: 
        f.append(translate(i))
    print(f)
    # let' translate the cataloge
    decodedWord=[]
    for i in WORDS:
        decodedWord.append(translate(i))
    #print(decodedWord)
    g = set()
    #test a and d then b and c
    for i in range(len(decodedWord)):
        if decodedWord[i] == f[1]:
            for j in range(len(decodedWord)):
                if decodedWord[j] == f[3]:
                    print("1-800-"+WORDS[i]+"-"+WORDS[j])
                    g.add("1-800-"+WORDS[i]+"-"+WORDS[j])
    for i in range(len(decodedWord)):
        if decodedWord[i] == f[0]:
            for j in range(len(decodedWord)):
                if decodedWord[j] == f[2]:
                    print("1-800-"+WORDS[i]+"-"+WORDS[j])
                    g.add("1-800-"+WORDS[i]+"-"+WORDS[j])
    return g
    
def translate(str) :
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    phone = "22233344455566677778889999"
    ret =""
    #print( str, len(str))
    for i in range(len(str)):
        #print(i)
        ret = ret +(phone[alpha.index(str[i])])
    return ret
