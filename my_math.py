
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

