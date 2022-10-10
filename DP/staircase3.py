def climbstairs(n):
    a = 1
    b = 1
    c = 2
    d = None
    for i in range(3,n+1):
        d = a + b +c
        a ,b , c = b, c, d
    return d