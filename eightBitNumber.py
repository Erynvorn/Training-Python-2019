import re

def eight_bit_number(n):
    print(n)
    if n == "":
        return False
    reg = re.compile(r'^[0-9]{1}$|^[1-9]{1}(\d){1}$|^[1]{1}\d\d$|^[2][0-4]{1}\d$|^[2][5]([0-5]){1}$')
    reg2 = re.compile(r'\s')
  
    return reg.search(n) != None and reg2.search(n) == None

