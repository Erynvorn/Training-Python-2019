def flatten(lst):
    ret = []
    for item in lst:
        if isinstance(item, (list)):
          ret.extend(item)
        else:
          ret.append(item)
    return ret

#flatten one level list

from itertools import chain
def flatten_and_sort(array):
    return sorted((chain(*array)))
