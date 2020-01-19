spam = ['apples', 'bananas', 'tofu' , 'pen', 'cats']


def eprint( doc):
    ret = ''
    for i in doc[:-1]:
        ret += i +', '
    ret += 'and '+ doc[-1]
    return ret

print(eprint(spam))
