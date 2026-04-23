
import unittest
#Deniel Test Case for Factorial Function
from my_math import factorial, sqrt, triangle_area, area_of_triangle

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

#Deniel test case for Musfira SQRT function
def test_sqrt_typical_deniel():
    result = sqrt(25)
    assert abs(result -5) < 0.0001

def test_sqrt_edge_deniel():
    assert sqrt(0) == 0
    assert sqrt(1) == 1

def test_sqrt_invalid_deniel():
    assert sqrt(-4) is None

# Kunga test cases

from my_math import abs_val, area_of_circle

def test_abs_val_kunga():
    assert abs_val(-5) == 5
    assert abs_val(10) == 10

def test_area_of_circle_kunga():
    assert area_of_circle(1) == 3.14
    assert area_of_circle(2) == 12.56

# Test cases by Musfira for Daniel's Original Function

def test_triangle_area_typical():
    assert triangle_area(10, 5) == 25.0

def test_triangle_area_edge_zero():
    assert triangle_area(0, 5) == 0
    assert triangle_area(5, 0) == 0

def test_triangle_area_invalid_negative():
    try:
        triangle_area(-3, 4)
        assert False
    except ValueError:
        assert True

# Musfira's Original function test Cases by Musfira

def test_area_triangle_typical():
    result = area_of_triangle(3, 4, 5)
    assert abs(result - 6) < 0.0001   # Heron's formula → area = 6

def test_area_triangle_edge():
    result = area_of_triangle(0.1, 0.1, 0.1)
    assert result is not None

def test_area_triangle_invalid_negative():
    assert area_of_triangle(-3, 4, 5) is None

def test_area_triangle_invalid_inequality():
    assert area_of_triangle(1, 2, 3) is None

# Test Cases for Kunga's Function by Musfira

def test_abs_val_edge_zero():
    assert abs_val(0) == 0

def test_abs_val_large_number():
    assert abs_val(-1000000) == 1000000



# Kunga test cases 

def test_abs_positive():
    assert abs_val(5) == 5

def test_abs_negative():
    assert abs_val(-5) == 5

def test_abs_zero():
    assert abs_val(0) == 0



# Area of circle tests
def test_area_of_circle_kunga():
    assert area_of_circle(1) == 3.14
    assert area_of_circle(2) == 12.56
