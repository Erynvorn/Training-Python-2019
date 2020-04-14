# 4 kyus Codewar

def recoverSecret(triplets):
    #triplets are two information sets: let's divide them in duos.
    d = []
    answer = ''
    for i in range(len(triplets)):
        for j in range(2):
            d.append([triplets[i][j], triplets[i][j+1]])   
            
    return duo(d,answer)   #call recursion

def duo(d,answer):
    if len(d) == 1:
        answer = answer + d[0][0] + d[0][1]
        return answer   #exit recurrence
    
    
    rem = ''            #looking for items in first position only.
    count ,fir ={}, {}
    for i in d:
        count.setdefault(i[1], 0)
        count[i[1]] = count[i[1]]
        fir.setdefault(i[0],0)
        fir[i[0]] = fir[i[0]]

    w =  {k : fir[k] for k in set(fir) - set(count) }  #finding the answer
    for k in w.keys():
        answer += k
        rem = k
        
    d = [ i for i in d if i[0] != rem]   #simplified duos by removing items starting with the latest answer
    
    res = []    #remove duplicate duos
    [res.append(x) for x in d if x not in res]
    
    return duo(res,answer)
    
"""
There is a secret string which is unknown to you.
Given a collection of random triplets from the string,
recover the original string.

A triplet here is defined as a sequence of three letters
such that each letter occurs somewhere before the next in
the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs
more than once in the secret string.

You can assume nothing about the triplets given to you
other than that they are valid triplets and that they contain
sufficient information to deduce the original string. In particular,
this means that the secret string will never contain letters that
do not occur in one of the triplets given to you."""

