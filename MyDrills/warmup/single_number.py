"""
SINGLE NUMBER
Pattern: HashMap frequency (or XOR trick)

Every element in the list appears exactly twice, except for one element
that appears only once. Find and return that single element.

Examples:
    single_number([2, 2, 1])       -> 1
    single_number([4, 1, 2, 1, 2]) -> 4

Think about: one simple approach counts how many times each value
appears. A slicker approach uses the XOR property: a ^ a = 0 and
a ^ 0 = a. Try the counting version first, then see if you can do it
without extra memory.
Contract:
The list is non-empty and contains integers (including negatives and zero).
Inputs that break the stated frequency rule are out of scope.

"""

from testkit import check, report


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result




if __name__ == "__main__":
    check("single at end", single_number([2, 2, 1]), 1)
    check("single at start", single_number([4, 1, 2, 1, 2]), 4)
    check("only one element", single_number([99]), 99)
    check("negatives included", single_number([-3, -3, 7]), 7)
    check("zero is the answer", single_number([0, 5, 5]), 0)
    check('negative answer', single_number([4, -7, 4]), -7)
    check('separated pairs', single_number([2, 0, 2, -1, 0]), -1)
    report()
