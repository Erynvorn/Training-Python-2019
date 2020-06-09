def reflections(x, y):
    m = max ( x, y)
    n = min (x,y)
    print(m,n)
    sx = 1
    sy = 1
    x += sx
    y += sy
    
    if x == 0 and y == 0:
        return True
    if x == m and y == n:
        return True
    if x == m and y == 0:
        return False
    if x == 0 and y == n:
        return False
    
    if y == n or y == 0:
        sy = -sy
    if x == m or x == 0:
        sx = -sx
    reflections(x,y)
