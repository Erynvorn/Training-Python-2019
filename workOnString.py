def work_on_strings(a,b):
    pass
    print(a,b)
    return work(a,b)+work(b,a)
    
def work(message,code):
    count = {}
    detail = []
    code = code.lower()
    for character in code:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    for i in range(len(message)):
        if  message[i].lower() in count.keys() and count[message[i].lower()]% 2 == 1:
            if message[i].lower() == message[i]:
                detail.append(message[i].upper())
            else:
                detail.append(message[i].lower())
        else:
            detail.append(message[i])
    return ''.join(detail)
    
    pass


def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)
