def to_camel_case(text):
    ret = ''
    l = 0
    if text == '':
        return ''
    text = text.replace('-',' ')
    text = text.replace('_',' ')
    if text[0] == text[0].lower():
        l = 1
    text = text.title()
    text = text.replace(' ','')
    print(text)
    if l == 1: 
        return text[0].lower() + text[1:]
    else:
        return text
     
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
