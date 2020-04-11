#spirals

a7 = [[1,1,1,1,1,1,1],[0,0,0,0,0,0,1],[1,1,1,1,1,0,1],[1,0,0,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
a6 = [[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,0,1],[1,0,0,1,0,1],[1,0,0,0,0,1],[1,1,1,1,1,1]]
a5 = [[1,1,1,1,1], [0,0,0,0,1] , [1,1,1,0,1] , [1,0,0,0,1], [1,1,1,1,1]]
a4 = [[1,1,1,1],[0,0,0,1], [1,0,0,1],[1,1,1,1]]
a3 = [[1,1,1], [0,0,1],[1,1,1]]
a2 = [[1,1], [0, 1]]

def nicePrint(a):

    i = 0
    j = 0
    l = len(a)
    while i < l:
        while j < l :
            print(a[i][j], end = '')
            j += 1
        print('')
        j=0
        i += 1


def addlayer(a,n):
    l = len(a)
    count = 1
    
# Expand the existing list

    # expand all in between by adding 2 at beginning and 2 char at the end

      
    # first line 1 1 and 0 1
    
    a[0].insert(0,1)
    a[0].insert(0,1)
    
    a[0].append(0)
    a[0].append(1)  #on second run the last line  is also modified

    print('modif first line')
    print(a)
    print(len(a))
    a[n-5].insert(0,0)
    a[n-5].insert(0,1)
    a[n-5].append(0)
    a[n-5].append(1)
    print('modif last line')  #the last line is modified with the first line. Very strange
    print(a)
    
    
    # second to last 1 0 and 0 1
    count = 0
    for count in range(1, n-5):
        a[count].insert(0,0)
        a[count].insert(0,1)
        a[count].append(0)
        a[count].append(1)

    

   

# Add on top and bottom

    # add two items at the beginning and the end of length l + 4
    # first all 1
    # second all zero but the last 1
    c=[0]* (n-1)
    c.append(1)
    a.insert(0,c)

    d = [1]*(n)
    a.insert(0,d)
    

    
    # second to last one then all zero
    c=[0]*(n-2)
    c.insert(0,1)
    c.append(1)
    a.append(c)
    # last all zero
    a.append(d)

    b = a.copy()
    ll = len(b)
    print('lenght of b')
    print(ll)
    b[2][ll-2] = 0
    b[ll-3][1] = 0
    b[ll-3][ll-2] = 0
    

    return b


def spiralize(size):
    
    if size % 4 == 0:
        counting = 4
        spiral = a4
        while counting != size:
            #nicePrint(spiral)
            print(spiral)
            spiral = addlayer(spiral,counting+4)
            counting += 4
            
    elif size % 4 == 1:
        counting = 5
        spiral = a5
        while counting != size:
            spiral = addlayer(spiral, counting+4)
            counting += 4

    elif size % 4 == 2:
        counting = 6
        spiral = a6
        while counting != size:
            spiral = addlayer(spiral, counting + 4)
            counting += 4

    elif size % 4 == 3:
        counting = 7
        spiral = a7
        while counting != size:
            spiral = addlayer(spiral, counting +4)
            counting += 4, 
    return spiral

nicePrint(spiralize(16))
#nicePrint(a7)
