def solve(n):
    note = [500, 200,100, 50, 20, 10]
    count = 0
    for i in note: 
        count += n // i
        n = n % i
        if n == 0:
            return count
            break
    return -1
    
    # Your code here
