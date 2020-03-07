import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    total = 1
    logging.debug('start fact program with '+str(n) +' and ' +str(total))
    print(fact(n,total))

def fact(n,t):
    if n>0:
        logging.debug('running fact with '+str(n) +' and ' +str(t))
        t *= n
        n -= 1
        return fact(n,t)
    return t

factorial(500)
