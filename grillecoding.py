def grille(message, code):
    decode = str((bin(code)))
    decode = decode[2:]
    de =[]
    ll=len(message)
    print('ll ', ll)
    if ll >= len(decode): 
        decode = '0' * (ll-len(decode))+ decode
    else :
        decode = decode[(len(decode)-ll):]
    sol = ""
    for i in range(len(message)) :
        #print(message[i], decode[i])
        if decode[i] == '1' :
            sol = sol+message[i]
    return sol

#Write a function that accepts two inputs: message and code and returns hidden message decrypted from message using the code.#
#The code is a nonnegative integer and it decrypts in binary the message.

#Grille("abcdef", 5)  => "df"

#message : abcdef
#code    : 000101
#----------------
#result  : df
