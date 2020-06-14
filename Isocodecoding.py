def checkkey(key):
    if len(key) != 10 : return -1
    test = []
    for i in range(10) :
        test.append(key[i])
    print(test)
    for i in test :
        if test.count(i) > 1 : return -1
    return 1

def isogram_encode(inp = True, key = 'missing'):
    input=str(inp)
    key = key.upper()
    #print('encode', inp,key)
    if checkkey(key) == 1: 
        if input != True and input != False and input != '':
            if (input.isdigit() == True):
                ret=''
                for i in input: ret += (key[(int(i)+9) % 10])
                return ret.upper()
            else: return 'Incorrect key or input!'
        else: return 'Incorrect key or input!'
    else: return 'Incorrect key or input!'

def isogram_decode(input = True, key = "missing"):
    nu = '1234567890'
    ret=''
    input = str(input).upper()
    #print('decode', input,key)
    key = key.upper()
    #print('decode', input,key)
    if checkkey(key) == 1 :
        if input != True and input != False and input != '':
            if input.isalpha() == True :
                for i in input: 
                    if key.find(i) != -1:    
                        ret += nu[key.index(i)]
                    else: return 'Incorrect key or input!'
                return ret
            else: return 'Incorrect key or input!'
        else: return 'Incorrect key or input!'
    else: return 'Incorrect key or input!'
    pass


