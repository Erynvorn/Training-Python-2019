def string_letter_count(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    ret = ''
    count = {}
    for character in s:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    
    for i in alpha:
        if i in count.keys():
            ret += str(count[i]) + i
    return ret


from collections import Counter

def string_letter_count(s):
    cnt = Counter(c for c in s.lower() if c.isalpha())
    return ''.join(str(n)+c for c,n in sorted(cnt.items()))
