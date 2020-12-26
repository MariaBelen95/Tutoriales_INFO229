import inverse

def test_inverse():
    s = 'hola'
    assert inverse.inverse(s) == 'aloh'

def test_inverse2():
    s = 'asfbia'
    assert inverse.inverse(s) == 'aibfsa'
