import min

def test_get_min():
    values = [1, 4, 2, 6]
    assert min.get_min(values) == 1

def test_get_min2():
    values = [14, 235, 123, 54, 2]
    assert min.get_min(values) == 2
