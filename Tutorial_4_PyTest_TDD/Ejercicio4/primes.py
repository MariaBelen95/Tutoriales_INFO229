import math

def is_prime(num):
    # Prime numbers must be greater than 1
    if num < 2:
        return False
    #Prime numbers mu
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

def sum_of_primes(values):
    sum = 0
    for val in values:
        if is_prime(val):
            sum += val
    return sum
