"""
CHALLENGE 16

A row of storage tanks sits side by side, each described by its wall
height (one unit apart). Choosing two walls forms a container, and the
water it can hold is limited by the shorter wall and the distance between
them. Given the wall heights, return the most water any pair of walls can
hold.

Examples:
    most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
    most_water([1, 1])                       -> 1

Contract:
Heights are non-negative integers. Fewer than two walls returns 0.
For indices i < j, the capacity is min(heights[i], heights[j]) * (j - i).

"""

from testkit import check, report


def most_water(heights):
    if len(heights) < 2:
        return 0
    left = 0
    right = len(heights) - 1
    result = 0
    while left < right:
        c_height = min(heights[left],heights[right])
        c_width = right - left
        result = max(result,c_height * c_width)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return result
        


if __name__ == "__main__":
    check("classic", most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check("two walls", most_water([1, 1]), 1)
    check("tall ends", most_water([4, 3, 2, 1, 4]), 16)
    check("small dip", most_water([1, 2, 1]), 2)
    check("empty", most_water([]), 0)
    check("single wall", most_water([5]), 0)
    check('zero walls', most_water([0, 0, 0]), 0)
    check('width matters', most_water([2, 1, 2]), 4)
    report()
