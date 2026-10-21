"""
TRIANGLE NUMBER CHECK
Pattern: Math / integer search

A triangular number counts dots arranged in rows of 1, 2, 3, ... dots.
For example, 6 = 1 + 2 + 3. Return True if the input is a triangular
number, otherwise False. The sequence starts 0, 1, 3, 6, 10, 15, 21, ...

Examples:
    is_triangle_number(6) -> True
    is_triangle_number(8) -> False
    is_triangle_number(0) -> True

Contract:
Non-negative integers may be very large. Negative numbers and non-integer
values return False. For this Python version, a float such as 6.0 is
accepted as an integer-valued number; 6.5 is not. Strings, None, and bool
values return False. No implicit conversion from text is allowed.

Think about: the total for m rows is m * (m + 1) // 2. Can you search
for m without constructing every previous triangular number? Use exact
integer arithmetic for large integers; floating-point roots can round.

Source: https://www.codewars.com/kata/557e8a141ca1f4caa70000a6
"""

from testkit import check, report


def is_triangle_number(n):       
    if type(n) == float:
        if(int(n) == n):
            n = int(n)
        else:
            return False    
    if not type(n) == int or n < 0:
        return False
    
    left = 0
    right = n
    
    while left <= right:
        mid = (left + right) // 2
        row_total = mid * (mid + 1) // 2
        if n < row_total:
            right = mid - 1
        elif n > row_total:
            left = mid + 1
        else:        
            return True

    return False


        
    




if __name__ == "__main__":
    check("three rows", is_triangle_number(6), True)
    check("incomplete rows", is_triangle_number(8), False)
    check("zero rows", is_triangle_number(0), True)
    check("one row", is_triangle_number(1), True)
    check("two is not triangular", is_triangle_number(2), False)
    check("negative", is_triangle_number(-6), False)
    check("fractional", is_triangle_number(6.5), False)
    check("integer-valued float", is_triangle_number(6.0), True)
    check("text is not a number", is_triangle_number("6"), False)
    check("none", is_triangle_number(None), False)
    check("bool is not a count", is_triangle_number(True), False)
    m = 10**20
    triangular = m * (m + 1) // 2
    check("very large triangle", is_triangle_number(triangular), True)
    check("just below large triangle", is_triangle_number(triangular - 1), False)
    check("just above large triangle", is_triangle_number(triangular + 1), False)
    report()
