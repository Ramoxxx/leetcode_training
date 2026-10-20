"""
CONTAINS DUPLICATE
Pattern: HashSet

Given a list of integers, return True if any value appears at least
twice, and False if every element is distinct.

Examples:
    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3, 4]) -> False

Think about: as you walk through the list, how do you remember which
values you have already seen? What lets you check "have I seen this?"
in one step?
Contract:
Input: a list of integers; it may be empty. Return a bool.

"""

from testkit import check, report


def contains_duplicate(nums):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("has a duplicate", contains_duplicate([1, 2, 3, 1]), True)
    check("all distinct", contains_duplicate([1, 2, 3, 4]), False)
    check("empty list", contains_duplicate([]), False)
    check("single element", contains_duplicate([7]), False)
    check("all same", contains_duplicate([5, 5, 5, 5]), True)
    check("duplicate at the end", contains_duplicate([1, 2, 3, 4, 2]), True)
    check('negative duplicate', contains_duplicate([-1, 0, -1]), True)
    report()
