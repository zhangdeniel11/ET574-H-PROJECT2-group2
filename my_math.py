
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


def main():
    raw = input("Enter a number for its factorial: ")

    try:
        num = int(raw)
        print(factorial(num))
    except (ValueError, TypeError) as x:
        print(x)


if __name__ == "__main__":
    main()
