# First write the while based code

from re import X
from tkinter import Y


def sum_digits(n):
    sum= 0
    while n!=0:
        sum += n%10
        n = n//10
    return sum

# Now try and implement this using recurtion.

def split(n):
    return n//10, n%10

def sum_digits_r(n):
    if n<10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits_r(all_but_last)+last
    
    # def new_sum(y):
    #     if n == 0: 
    #         print(y)
    #     else:
    #         y += n%10
    #         return rec_sum_digits(n//10)
    # return new_sum