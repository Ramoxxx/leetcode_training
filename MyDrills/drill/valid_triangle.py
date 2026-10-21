"""
VALID TRIANGLE (three side lengths)
Pattern: Logic (triangle inequality)

The inputs are integers. Zero and negative lengths are invalid.
Three positive lengths can form a valid triangle if the sum of the two
shorter sides is strictly greater than the longest side. Given exactly
three numbers, return True if they can form a triangle, otherwise False.

Examples:
    is_triangle(3, 4, 5)  -> True
    is_triangle(1, 2, 3)  -> False   (1 + 2 is not > 3)
    is_triangle(7, 2, 2)  -> False

Think about: if you sort the three sides, the rule reduces to one
comparison: shortest + middle > longest. Watch the strict inequality.
"""

from testkit import check, report


def is_triangle(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return False
    sides = [a,b,c]
    sides.sort()
    return sides[0] + sides[1] > sides[2]


if __name__ == "__main__":
    check("valid triangle", is_triangle(3, 4, 5), True)
    check("degenerate", is_triangle(1, 2, 3), False)
    check("too flat", is_triangle(7, 2, 2), False)
    check("equilateral", is_triangle(5, 5, 5), True)
    check("zero side", is_triangle(0, 4, 5), False)
    check("order does not matter", is_triangle(5, 3, 4), True)
    check('negative side', is_triangle(-1, 2, 2), False)
    check('two zero sides', is_triangle(0, 0, 1), False)
    report()
