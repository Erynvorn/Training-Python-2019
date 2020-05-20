def split_and_add(numbers, n):
    ret = []

    p = 0  # pair impair
    if n == 0 or len(numbers) == 1:
        return numbers
    while True:
        
        if n == 0 or len(numbers) == 1:
            return numbers
        l = len(numbers)
        if l % 2 == 0 :
            m = int(l / 2)
            fi = numbers[:m]
            se = numbers[m:]
            p = 0
        else:
            fi = numbers[:int((l-1)/2)]
            se = numbers[int((l-1)/2):]
            p = 1
        
        for i in range(len(fi)):
            ret.insert(0,fi[-1-i]+se[-1-i])
        if p == 1:
            ret.insert(0,se[0])
        n -= 1
        numbers = ret
        ret =[]


def split_and_add(numbers, n):
    for _ in range(n):
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]
        numbers = [a + b for a, b in zip((len(right) - len(left)) * [0] + left, right)]
        if len(numbers) == 1:
            return numbers
    return numbers
