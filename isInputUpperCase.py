# iis the input uppercase

def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False


print(is_uppercase('HELLO'))
