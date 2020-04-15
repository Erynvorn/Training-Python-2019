def parse_bank_account(b):
    l= len(b)
    print(l)
    print(b)
    n= int((l-3)/9)
    print(n)
    ret =''
    t= { 1 :'     |  |', 2:' _  _||_ ', 3:' _  _| _|', 4:'   |_|  |', 5:' _ |_  _|', 6:' _ |_ |_|', 7 : ' _   |  |' , 8: ' _ |_||_|', 9:' _ |_| _|', 0:' _ | ||_|' }
    for i in range(n):
        num =' '+b[i*3+1]+' '+b[i*3+3*n+1]+b[i*3+3*n+2]+b[i*3+3*n+3]+b[i*3+6*n+2]+b[i*3+6*n+3]+b[i*3+6*n+4]
        print(num)
        for k,v in t.items():
            if v == num:
                ret +=str(k)
                #print('Yahoo')
        #    if num == v:
        #        print(k)
    if ret != '':
        ret = int(ret)
    else: 
        return 0    
    return ret

"""
Parse bank account
You work for a bank, which has recently purchased an ingenious machine to assist in reading letters and faxes sent in by branch offices.
 The machine scans the paper documents, and produces a string with a bank account that looks like this:

 _     _  _     _  _  _  _  _
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
 Each string contains an account number written using pipes and underscores.
 Each account number should have at least one digit, all of which should be in the range 0-9.

 Your task is to write a function that can take bank account string and parse it into actual account numbers.

 @param {string} bankAccount
 @return {number}
 """
