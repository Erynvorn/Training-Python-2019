def find_uniq(arr):
    count = {}
    for number in arr:
        count.setdefault(number,0)
        count[number] += 1
    for k,v in count.items():
        if v == 1:
            return k
