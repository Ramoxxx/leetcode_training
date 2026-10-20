"""
PRODUCT OF ARRAY EXCEPT SELF
Pattern: Arrays (prefix / suffix products)

Given a list of integers, return a new list where each position holds
the product of every other element (everything except the element at
that position). Do it WITHOUT using division.

Examples:
    product_except_self([1, 2, 3, 4])  -> [24, 12, 8, 6]
    product_except_self([-1, 1, 0, -3, 3]) -> [0, 0, 9, 0, 0]

Walkthrough of the first example:
    index 0 -> 2*3*4 = 24
    index 1 -> 1*3*4 = 12
    index 2 -> 1*2*4 = 8
    index 3 -> 1*2*3 = 6

Think about: for each index, the answer is (product of everything to
the LEFT) times (product of everything to the RIGHT). Compute the left
products in one pass, the right products in another, and multiply.
Contract:
The input contains at least two integers; negatives and zeros are allowed.
Return a list of integers. Required time: O(n), without division.
Bonus: O(1) extra space, excluding the returned list.

"""

from testkit import check, report


def product_except_self(nums):
    left_prod = 1
    result = [1]*len(nums)
    for i in range(len(nums)):
        result[i] = left_prod
        left_prod *= nums[i]
    right_prod = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= right_prod
        right_prod *= nums[i]
    return result
        


if __name__ == "__main__":
    check("basic", product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
    check("contains a zero", product_except_self([-1, 1, 0, -3, 3]),
          [0, 0, 9, 0, 0])
    check("two elements", product_except_self([3, 7]), [7, 3])
    check("with ones", product_except_self([1, 1, 1]), [1, 1, 1])
    check('two zeros', product_except_self([0, 2, 0, 4]), [0, 0, 0, 0])
    check('all negative', product_except_self([-1, -2, -3]), [6, 3, 2])
    check('zero at start', product_except_self([0, 2, 3]), [6, 0, 0])
    report()
