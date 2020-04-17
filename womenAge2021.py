def womens_age(n):
    for i in range(n):
        if n == (2*i) or n == (2*i+1):
            return str(n)+'? That\'s just '+str(n%i+20)+', in base '+str(i)+'!'
    pass
