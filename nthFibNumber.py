def nth_fib(n):
    # your code
    print(n)
    Fib = [0 ,1]
    for i in range (2, n ):   # generating Fn Fn+1 which is sum of Fn ** 2
        a = Fib[i-2]
        b = Fib[i-1]
        Fib.append(Fib[i-2]+Fib[i-1])
    return Fib[n-1]
