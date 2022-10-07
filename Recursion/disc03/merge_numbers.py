""" Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """


# Most Optimized

def merge_numbers(x,y):
    if y == 0:
        y=''
    return int(''.join(sorted(str(x)+str(y))[::-1]))
