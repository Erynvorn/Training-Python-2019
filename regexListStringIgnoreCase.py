import re

def search(titles, term): 
    reg = re.compile(term, re.IGNORECASE)
    ret= []
    for i in titles:
        if reg.search(i) != None:
            ret.append(i)
    return ret

#search list for string
