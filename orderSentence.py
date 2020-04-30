def order(sentence):
    ret = []
    text = sentence.split()
    for i in range(1,len(text)+1):
        for j in range(len(text)):
            if str(i) in text[j]:
                ret.append(text[j])
    return ' '.join(ret)

