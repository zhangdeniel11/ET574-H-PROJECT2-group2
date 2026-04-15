
import unittest

from my_math import factorial, sqrt

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

# Musfira's Core Function Unittest by Musfira 
def test_sqrt_typical():

    result = sqrt(9)
    assert abs(result - 3) < 0.0001

def test_sqrt_edge():

    assert sqrt(0) == 0

def test_sqrt_invalid():

    assert sqrt(-1) is None
