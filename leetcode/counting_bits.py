'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''
# One Solution

l = []

def counting_bits(n,i=0):
    if i>n:
        return l
    else:    
        l.append(helper(i))
        return counting_bits(n,i+1)

# def counting(n,i=0):
#     l = []
#     if i>n:
#         return l
#     else:
#         print(i)
#         return counting(n,i+1)

def helper(n):
    l = bin(n)
    l=int(l[2:len(l)])
    return count_digits(l)
    
    
def split(n):
    return n//10, n%10

def count_digits(n):
    if n<10:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return n
    else:
        except_last, last = split(n)
        return count_digits(except_last)+last
    
    
# Second Solution

def countBits(n):
    res = []
    binary = ''
    for i in range(0,n+1):
        binary = str(bin(i).count('1'))
        res.append(binary)
    return res