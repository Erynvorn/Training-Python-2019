def tribonacci(s, n):
    
        """Print a Tribonacci series up to n."""
        if n == 0 : return []
        elif n == 1 : return s[0:1]
        elif n == 2 : return s[0:2]
        elif n == 3 : return s
        else :
            a, b, c = s[0], s[1], s[2]
            i = 0
            ret = s[:]
            while i < n-3:
                a, b,c = b,c, a+b+c
                ret.append(c)
                i+=1
            return ret
