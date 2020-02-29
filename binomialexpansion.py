#binomial expansion 3kyu python codewars 25 August 2018

def trianglepascal(n,p):
    if (n == 0 and p == 0) : return 1
    elif ( n == 0 and p != 0) :return 0
    else :
        return trianglepascal(n-1,p)+trianglepascal(n-1, p-1)


def expand(expr):
    print(expr)
    x=""
    po =expr.index("^")
    p = int(expr[po+1:])
    
    for i in expr : 
        if i.isalpha(): 
            x = i
            y = expr.find(x)
    if y == 1 : 
        a = 1
    elif (y == 2 and expr[1] == '-') :
        a = -1
    else :
        a = int(expr[1:y])
        
    if po-1 == y+1 :
        b = 0
    else:
        b = int(expr[y+1:po-1])

    if p == 0 : return '1'
    else :
        expo =[]
        count = 0
        while count <= p :
            expo.append((a**(p-count)) * (b**count) * trianglepascal(p,count))
            count += 1
        
        counter =1
        result = ""
        
        if (expo[0] == 1 and p > 1):
            result =  x +"^"+str(p)
        elif (expo[0] == -1 and p> 1):
            result = '-'+x+'^'+str(p)
        elif (abs(expo[0]) != 1 and p > 1) :
            result =  str(expo[0]) + x +"^"+str(p)
        elif (abs(expo[0]) == 1 and p == 1) :
            result = x
        elif (abs(expo[0]) != 1 and p == 1) :
            result = str(expo[0]) + x
            
        while counter < p-1 :
            if expo[counter] < 0 :
                result = result + str(expo[counter]) + x +"^"+str(p-counter)
            elif expo[counter] == 1 : 
                result = result + "+" + x +"^"+str(p-counter)
            else :
                result = result + "+"+ str(expo[counter]) + x +"^"+str(p-counter)
            counter += 1
        
        if (expo[p-1] < 0  and p > 1):
                result = result + str(expo[p-1]) + x 
        elif (expo[p-1] == 1  and p> 1): 
                result = result + "+" + x 
        elif (expo[p-1] > 1 and p>1) :
                result = result + "+"+ str(expo[counter]) + x 
        
            
        if expo[p] < 0 :
                result = result + str(expo[p])
        else :
                result = result + "+"+ str(expo[p])
        #print( a, x, " + " , b , " power ", p) 
        print(expo)
        return result
        
        pass
