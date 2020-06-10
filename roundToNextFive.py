def round_to_next5(n):
    print(n)
    for i in range(5):
        if n % 5 == 0:
            return n
        n+=1
    
def round_to_next5(n):
    return n + (5 - n) % 5
