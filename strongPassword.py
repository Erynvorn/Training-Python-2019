test = 'slkghjslkghsgslkh1Qkghsl23#'

testweak1 = 'dklghaghlgk'
testweak2 = 'sljkhglkhgSGSGgsgg'
testweak3 = '#$#@'

import re

lowRegex = re.compile(r'[a-z]')
highRegex = re.compile(r'[A-Z]')
speRegex = re.compile(r'[!@#$%^&*()_+,<.>/?]')


def strongPassword(input):
    if len(input)>7:
        if lowRegex.search(input) !=None:
            if highRegex.search(input) != None:
                if speRegex.search(input) != None:
                    print(input + ' : good password')
                    return
    print(input + ' : Bad Password')

strongPassword(test)
strongPassword(testweak1)
strongPassword(testweak2)
strongPassword(testweak3)
strongPassword('ErqRERETY12*')
print(highRegex.search(testweak1))

