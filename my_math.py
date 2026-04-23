
# Core Function by Musfira

"""
Function Name: sqrt
Purpose: Compute the square root of a non-negative number x without using the math module.
Parameters:
    x (float or int): A non-negative number whose square root will be computed.
Return Value:
    float: The approximate square root of x, or None for invalid input.
"""

def sqrt(x):

    if x < 0:
        return None
    if x == 0 or x == 1:
        return x

    low = 0
    high = x
    tolerance = 0.000001

    while high - low > tolerance:
        mid = (low + high) / 2
        if mid * mid > x:
            high = mid
        else:
            low = mid

    return (low + high) / 2

# Original Function by Musfira

"""
Function Name: area_of_triangle
Purpose: Compute the area of a triangle using Heron's formula.
Parameters:
        a (float): Length of side a (must be positive)
        b (float): Length of side b (must be positive)
        c (float): Length of side c (must be positive)
Return Value:
    float: The area of the triangle, or None if the sides do not form a valid triangle.
"""

def area_of_triangle(a, b, c):

    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return None

    # Triangle inequality check
    if a + b <= c or a + c <= b or b + c <= a:
        return None

    # Semi-perimeter
    s = (a + b + c) / 2

    #formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

#Core Function - Deniel
"""Function Name - Factorial 
Calculates the factorial of the number as long as it is non negative
Factorial is the product of all positive numbers from 1 up to the number
(num) is the parameter that is the factorial being calculated
return value - int: the factorial of the input number (num)

Error Check - TypeRaise - checks if the input is not integer
Value Error - Checks if input is negative
"""

def factorial(num):
        if not isinstance(num,int):
            raise TypeError("Input has to be an integer")
        if num < 0:
            raise ValueError("Factorial does not exist for negative numbers")
        
        if num == 0:
            return 1
        
        fact = 1
        for i in range(1, num+1):
            fact *=i
        
        return fact



#Original Function - Deniel
"""Function Name - Triangle Area
Calculates the area of a triangle given its base and height
Paramters - Takes in Base and Height of the triangle, must be either int or float and must be non negative
return value - float: the area of the triangle
Type Error - checks if the input is not a number
Value Error - checks if the input is negative"""
def triangle_area(base,height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non negative")

    return 0.5 * base * height


    # Kunga - Core Function
def abs_val(x):
    if x < 0:
        return -x
    return x

# Kunga - Original Function
def area_of_circle(r):
    return 3.14 * r * r