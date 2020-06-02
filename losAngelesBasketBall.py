import re

def get_los_angeles_points(results):
    tot = 0
    reg = re.compile(r'^Los Angeles\s[A-Z][a-z]+$')
    for i in results:
        if reg.search(i[0]) != None:
            print(i[1])
            c = i[1].index(':')
            print(c)
            tot += int(i[1][:c])
    return tot
    #your code here

def get_los_angeles_points(results):
    pattern = re.compile('Los Angeles [A-Z][a-z]+')
    return sum(int(k[1].split(':')[0]) for k in results if pattern.fullmatch(k[0]))
