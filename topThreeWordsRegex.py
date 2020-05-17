import re

def top_3_words(text):
    text=text.replace("_"," ")
    #print(text)
    text = text.lower()
    test = re.compile(r'(\'*?\w+\'?\w*\'?\w*)')
    u = test.findall(text)
    count={}
    for character in u:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    
    if '_' in count.keys():
        del count['_']
    print(count)
    
    #largest
    maxValue = ''
    maxVal2 = ''
    maxVal3 = ''
    max = 0
    for v,k in count.items():
        if k > max :
            maxValue = v
            max = k
    max2 = 0
    for v,k in count.items():
        if k > max2 and k <= max and v !=maxValue :
            maxVal2 = v
            max2 = k
    
    
    max3 = 0
    for v,k in count.items():
        if k > max3 and k <= max2 and v != maxValue and v != maxVal2 :
            maxVal3 = v
            max3 = k
        
        
    
    
    if len(count) == 0:
        return []
    if len(count) == 1:
        return [maxValue]
    elif len(count) == 2:
        return [maxValue, maxVal2]
    else:
        return [maxValue, maxVal2, maxVal3]
        
