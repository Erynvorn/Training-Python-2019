def snaprec(flash_pile, turtle_pile, nsnap) :
    i = min(len(flash_pile), len(turtle_pile))
    print("i " ,i)
    print("nsnap ", nsnap)
    print("player 1 : " , flash_pile)
    print("player 2 : " , turtle_pile)
    if i == 0 : return nsnap
    if i == 1 : 
        print("coucou")
        if turtle_pile[0] == flash_pile[0] :
            print("nsnap i = 1", nsnap)
            nsnap += 1
            return nsnap
        else: 
            print("pas les memes i=1", nsnap)
            return nsnap
    print("passage")
    j = 0 
    while j < i :
        if (j>0 and (turtle_pile[j-1] == flash_pile[j])):
            #snap
            nsnap += 1
            #add played card to flash deck
            count=0
            while count < j:
                flash_pile.append(flash_pile[count])
                flash_pile.append(turtle_pile[count])
                count +=1
            flash_pile.append(flash_pile[j])
            #turn around
            return snaprec(flash_pile[j+1:],turtle_pile[j:],nsnap)
            
        if turtle_pile[j] == flash_pile[j] :
            #snap
            nsnap += 1
            #add played card to flash deck
            count = 0
            while count  <= j :
                flash_pile.append(flash_pile[count])
                flash_pile.append(turtle_pile[count])
                count +=1
            #turn and start again with less card
            #print(turtle_pile[j+1:])
            #print(flash_pile[j+1:])
            #derniere carte ?
            if i == 1 : return nsnap 
            else :
                return snaprec(flash_pile[j+1:],turtle_pile[j+1:],nsnap)
        
        j += 1
    return nsnap
        
def snap(flash_pile, turtle_pile):
    return snaprec(flash_pile, turtle_pile, 0)

