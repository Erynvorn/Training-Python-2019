testtext = 'https://lkghalkgh.com http://www.cnn.com www.abc.com'

import re,pyperclip

# urlRegex = re.compile(r'(http)(s)?(://)(\w+\.)?(\w+)')
urlRegex = re.compile(r'(http)(s)?(://)([a-zA-Z0-9.]+)')  # works for 1 and 2
wwwRegex = re.compile(r'(www.)([a-zA-Z0-9.]+)')

testtext =str(pyperclip.paste())
matches =[]
for groups in urlRegex.findall(testtext):
    urltext= ''.join(groups)
    matches.append(urltext)

for groups in wwwRegex.findall(testtext):
    wwwtext= ''.join(groups)
    matches.append(wwwtext)

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('No URL recognized')

