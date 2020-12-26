from primes import is_prime
from primes import sum_of_primes

#Si introducimos 1, entonces no debe ser un número primo.
def test_prime_number():
    assert is_prime(1) == False

def test_prime_number_2():
    assert is_prime(29)

def test_prime_other_number():
    assert is_prime(15) == False

def test_sum():
    sum_of_primes([2, 1, 5, 3, 6, 7]) == 17

def test_sum_2():
    sum_of_primes([3, 2, 5, 8, 31, 11, 53]) == 105

def test_sum():
    sum_of_primes([0, 1, 4, 6, 8]) == 0
