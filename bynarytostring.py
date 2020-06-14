def binary_to_string(binary):
    print(len(binary))
    print(binary.count('b'))
    i=1
    ret=''
    t=binary.split('0b')
    print(t)
    while i < len(t) :
        ret +=(chr(int(t[i], base =2)))
        i += 1
    return ret
        
    print ( chr(0b1000011))
    # insert your code here



def binary_to_string(binary):
    return ''.join( chr(int(b, 2)) for b in binary[2:].split('0b') )
