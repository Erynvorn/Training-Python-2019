#ENCODING MD5

import hashlib

def pass_hash(str):
    s = bytes(str, encoding="ascii")
    return hashlib.md5(s).hexdigest()

print(pass_hash('daniel seite'))
