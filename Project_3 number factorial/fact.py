# create function which calculate factorial of numbers

def fact(n):
    if n == 1:
        return 1

    # call inner function
    return fact(n-1) * n

print(fact(5))