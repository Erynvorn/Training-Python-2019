import re

def calculate_string(st): 
    second = re.compile(r'[0-9\.\+\-\*\/]')
    s = second.findall(st)
    print(s)
    fi = 0
    se = 0
    for i in range(len(s)):
        if s[i] in '+-/*':
            fi = float(''.join(s[:i]))
            se = float(''.join(s[i+1:]))
            op = s[i]
    if op == '+':
        return str(round(fi+se))
    elif op == '-':
        return str(round(fi-se))
    elif op == '*':
        return str(round(fi*se))
    elif op == '/':
        return str(round(fi/se))
