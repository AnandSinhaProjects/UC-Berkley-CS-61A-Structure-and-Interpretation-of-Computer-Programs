from itertools import count


def get_digits(n): #Let's say that n is a integer.
    l = digit_list(n)
    l = l[::-1]
    sum = 0
    for i in range(0,len(l)):
        if i%2==0:
            temp = l[i]*2
            if temp>=10:
                ln = digit_list(temp)
                sum += get_sum(ln)
            else:
                sum += temp
        else:
            sum += l[i]
    return sum   
                
                
def digit_list(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n//10
    return l

def get_sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum