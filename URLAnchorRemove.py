import re

def remove_url_anchor(url):
    test = re.compile(r'(#.*)')
    return test.sub('',url)
    # TODO: complete
