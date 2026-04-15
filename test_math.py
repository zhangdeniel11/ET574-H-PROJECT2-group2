from my_math import factorial

def test_factorial1():
    assert factorial(5) == 120

def test_factorial2():
    assert factorial(0) == 1

def test_factorial3():
    try:
        factorial(-1)
        assert False
    except ValueError:
        assert True