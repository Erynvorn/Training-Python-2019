def number(lines):
    
    if lines == []:
            return []
    ret =[]
    count = 1
    for i in lines:
        ret.append(str(count)+": "+i)
        count += 1
    return ret

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
