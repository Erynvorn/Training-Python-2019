def duplicate_count(text):
    text = text.upper()
    message = []
    count = {}
    ret = 0
    for i in text:
        message.append(i)
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    for k,v in count.items():
        if v > 1:
            ret += 1
    return ret
