test = '   lskjhsjlkh  '

import re  #import Regex tools



def myStrip(input, subText=''):    #if subText='' strip() else remove subText
    if subText == '':
        exspaceRegex = re.compile(r'(\s+)*(.*)(\s+)*')
        return exspaceRegex.search(input).group(2)
    else:
        subRegex = re.compile(subText)
        return subRegex.sub('', input)

print(myStrip('sklghlkfh    kljlkfzj    ', 'l'))
print(myStrip('sklghlkfh    kljlkfzj    ', 'kl'))
print(myStrip('     sklghlkfh    kljlkfzj   '))
