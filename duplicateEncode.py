ef duplicate_encode(word):
    word = word.lower()
    count = {}
    
    for i in range(len(word)):    # use a dictionary to register all occurences
        count.setdefault(word[i], 0)
        count[word[i]] = count[word[i]] + 1
        
    ret = ''
    for i in range(len(word)):    # read the dictionary to provide answer
        if count[word[i]] > 1:
            ret += ')'
        else:
            ret += '('
    return ret
