#One Solution

def fibonacci(self,n,prev=0,new=1,i=0):
    if i == n:
        return prev
    else:
        fibonacci(n,new,new+prev,i+1)
        
# Second Solution

def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n>1:
            return self.fib(n-1)+self.fib(n-2)