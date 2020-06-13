def countO(x,one):
    if x < 2 : return one+x
    else:
        one += 2**(len(bin(x))-3)-1
    return countO(x-2**(len(bin(x))-3),one)
    
def countOnes(left, right):
    print(len(bin(left)))
    print(left-2**(len(bin(left))-3))
    return countO(right,0) - countO(left,0)
    #for i in range(100):
     #   print(bin(i))
        #print(bin(21))
        #print(bin(10))
        #print(bin(18))
    # Your code here!
    return 0
