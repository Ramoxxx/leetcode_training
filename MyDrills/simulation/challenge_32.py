"""
CHALLENGE 32

A layout engine needs the side length of the largest square that fits
inside a given area, rounded down to a whole number. In other words,
given a non-negative integer, return the integer part of its square root.
You may not use any built-in square-root function.

Examples:
    int_sqrt(8)   -> 2   (since 2*2=4 <= 8 < 9=3*3)
    int_sqrt(100) -> 10

Contract:
The input is a non-negative integer. Return an integer, not a float.
Do not use sqrt, isqrt, or fractional powers such as area ** 0.5.

"""

from testkit import check, report


def int_sqrt(area):
    if area < 2:
        return area
    left = 2
    right = area // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if area < square:
            right = mid - 1
        elif area > square:
            left = mid + 1
        else:
            return mid    

    return left - 1
    


if __name__ == "__main__":
    check("perfect square", int_sqrt(4), 2)
    check("rounds down", int_sqrt(8), 2)
    check("zero", int_sqrt(0), 0)
    check("one", int_sqrt(1), 1)
    check("hundred", int_sqrt(100), 10)
    check("just below", int_sqrt(99), 9)
    check("large value", int_sqrt(2147395600), 46340)
    check('large square boundary', int_sqrt(10**40 - 1), 99999999999999999999)
    report()
