#testing requests

import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem: %s' % (exc))
print('Oups')
