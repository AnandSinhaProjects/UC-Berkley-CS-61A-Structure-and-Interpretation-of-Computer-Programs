# A simple example of Recustion is ->

def print_all(x):
    print(x)
    return print_all

# Lets look at a beter example for the same example -> 
def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum
