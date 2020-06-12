def flatten(lst):
    ret = []
    for item in lst:
        if isinstance(item, (list)):
          ret.extend(item)
        else:
          ret.append(item)
    return ret

#flatten one level list

def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])
