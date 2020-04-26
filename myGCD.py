
def mygcd(x, y):
    if x < y:
        x,y = y, x
    if y == 0:
        return x
    return mygcd(y, x%y)
    
    """
    One way to find the GCD of two numbers is Euclid’s algorithm, 
    which is based on the observation that if r is the remainder 
    when a is divided by b, then gcd(a, b)= gcd(b, r). 
    As a base case, we can use gcd(a, 0) = a."""
    
