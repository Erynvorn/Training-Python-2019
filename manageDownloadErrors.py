#manage download errors

import requests
res=requests.get('http://inventwithpython.com/page_does_not_exist')

try:
    res.raise_for_status()
except Exception as exc:
        print('There was aproblem: %s' % (exc))

        
