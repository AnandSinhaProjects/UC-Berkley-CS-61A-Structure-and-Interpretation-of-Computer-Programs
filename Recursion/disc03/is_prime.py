# Method 1 

def is_prime(n):
    if get_factors(n) == 2:
        return True
    else:
        return False
    
def get_factors(n,count=0,i=1):
    if i>n:
        return count
    else:
        if n%i == 0:
            return get_factors(n,count+1,i+1)
        else:
            return get_factors(n,count,i+1)

#Method 2 

def is_prime_2(n):
    def helper(i):
        print(i)
        if i==n:
            return True
        elif n%i == 0:
            return False
        return helper(i+1)
    return helper(2)