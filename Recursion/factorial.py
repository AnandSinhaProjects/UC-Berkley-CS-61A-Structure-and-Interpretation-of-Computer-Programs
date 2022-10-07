# FIrst we write the code for finding factorial using loops.

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans

# Now we try to write the code using the recursive function.

def factorial_r(n):
    if n == 0:
        return None
    else:
        return n*factorial(n-1)