def is_vow(inp):

    for i in range(len( inp)) :
        if inp[i] in ['a','e','i','o','u']:
            inp[i] = ord(inp[i])
        elif inp[i] in [97,101,105,111,117]:
            print(inp[i], chr(i))
            inp[i] = chr(inp[i])
    return inp
    pass
