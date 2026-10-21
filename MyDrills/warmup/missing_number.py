"""
MISSING NUMBER
Pattern: Math (sum formula) or Set

Given a list containing n distinct numbers taken from the range
0, 1, 2, ..., n (so exactly one number in that range is missing),
return the missing number.

Examples:
    missing_number([3, 0, 1])       -> 2
    missing_number([0, 1])          -> 2
    missing_number([9,6,4,2,3,5,7,0,1]) -> 8

Think about: the numbers 0..n have a known total (n * (n + 1) // 2).
If you compare that to the actual sum of the list, what does the
difference tell you? A Set-based approach also works.
Contract:
The empty list is allowed: n = 0 and the missing number is 0.

"""

from testkit import check, report


def missing_number(nums):
    nums.sort()
    nums.append(len(nums)+1)
    for i in range(0,len(nums)):
        if i != nums[i]:
            return i
    


if __name__ == "__main__":
    check("missing middle", missing_number([3, 0, 1]), 2)
    check("missing the top", missing_number([0, 1]), 2)
    check("longer case", missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
    check("missing zero", missing_number([1]), 0)
    check("single zero present", missing_number([0]), 1)
    check('empty range', missing_number([]), 0)
    check('zero missing from longer list', missing_number([3, 1, 2]), 0)
    report()
