def reverse_bits(n):
    nn = str(bin(n))
    m = []
    print(nn)
    for i in range(2,len(nn)):
        m.append(nn[i])
    m.append("b")
    m.append("0")
    m.reverse()
    return int(''.join(m),2)
    # your code here
    pass


def reverse_bits(n):
    return int(''.join(reversed(bin(n)[2:])), 2)
