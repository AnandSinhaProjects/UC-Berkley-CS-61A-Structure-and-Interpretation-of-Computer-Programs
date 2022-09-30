def find_prime(n):
    """Print the prime factors of n in non-decreasing order.
    >>> prime factors(8)
    2
    2
    2
    >>> prime_factors (9)
    3
    3
    >>> prime_factors (10)
    2
    5
    >> prime_factors (11)
    >>> prime_factors (12)
    2
    2
    3
    >>> prime_factors (858)
    2
    3
    11
    13
    """
    lowest_prime = 2
    while n!=1:
        if n%lowest_prime == 0:
            n = n/lowest_prime
            print(lowest_prime)
        else:
            lowest_prime += 1
            continue

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()