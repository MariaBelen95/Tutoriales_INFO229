import fibonacci

def test_fibonacci():
    n = 3
    assert fibonacci.fibonacci(n) == 1

def test_fibonacci2():
    n = 6
    assert fibonacci.fibonacci(n) == 5

def test_fibonacci3():
    n = 8
    assert fibonacci.fibonacci(n) == 13
