def anagrams(word, words):
    message = []
    count = {}
    ret = []
    
    for i in word:
        message.append(i)
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
        
    for i in range(len(words)):
        messages = []
        counts = {}
        for j in words[i]:
            messages.append(j)
        for character in messages:
            counts.setdefault(character, 0)
            counts[character] = counts[character] + 1
        if count == counts:
            ret.append(words[i])
        
    return ret
