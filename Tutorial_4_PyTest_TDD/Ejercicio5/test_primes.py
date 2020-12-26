from primes import is_prime

#Si introducimos 1, entonces no debe ser un número primo.
def test_prime_number():
    assert is_prime(1) == False

def test_prime_number_2():
    assert is_prime(29)

def test_prime_other_number():
    assert is_prime(15) == False
