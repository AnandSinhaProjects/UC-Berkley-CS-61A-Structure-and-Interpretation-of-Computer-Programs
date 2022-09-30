# Fibonacci number - 0 1 1 2 3 5 8 13 21 34 55

def fib(n):
    priv, next = 0 , 1
    for i in range(n-3):
        if priv == 0:
            print(priv) # 0
            print(next) # 1
            priv = next
            print(next)
        else:
            next+= priv # 2
            print(next) # 2
            priv += next
            print(priv) # 3
            
            
            
            
            