test = 'Satoshi Nakamoto Alice Nakamoto RoboCop Nakamoto'
test2 = 'satoashi Nakamoto Mr. Nakamoto'
test3 = 'Nakamoto'

import re

SakRegex = re.compile(r'[A-Z][a-zA-Z]+\sNakamoto')

mo = SakRegex.findall(test)
print(mo)
print(SakRegex.findall(test2))
print(SakRegex.findall(test3))
