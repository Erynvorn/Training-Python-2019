def productFib(prod):
    # your code
    print(prod)
    max = 110
    ret = []
    Fib = [ 0 ,1]
    Fsq = [0 , 1]
    for i in range (2, max):   # generating Fn Fn+1 which is sum of Fn ** 2
        a = Fib[i-2]
        b = Fib[i-1]
        Fib.append(Fib[i-2]+Fib[i-1])
        Fsq.append(Fib[i]*Fib[i]+Fsq[i-1])
    
    for i in range(0,max):     #testing and returning
        if Fsq[i] == prod:
            ret.append(Fib[i])
            ret.append(Fib[i+1])
            ret.append(True)
            break
        elif Fsq[i] > prod:
            ret.append(Fib[i])
            ret.append(Fib[i+1])
            ret.append(False)
            break
    return ret

"""
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.

"""
