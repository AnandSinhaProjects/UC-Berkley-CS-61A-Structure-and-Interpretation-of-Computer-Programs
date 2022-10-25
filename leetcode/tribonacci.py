# def tribonacci(n,prev=0,new=1,i=0,l=[]):
#     ltest = l
#     ltest.append(prev)
#     if len(l)>=n:
#         # sum=0
#         # for i in range((len(l)-1)-n,len(l)-1):
#         #     sum+=l[i]
#         print(len(l))
#         return None
#     tribonacci(n,new,prev+new,i+1,ltest)

# Redundant Code Above

'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 
'''

# 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 
# 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 
# 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 
# 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852… so on.

def tribonacci(n,n1=0,n2=1,n3=1,i=0):
    if i>=n:
        print(n1)
        return None
    else:
        return tribonacci(n,n2,n3,n1+n2+n3,i+1)