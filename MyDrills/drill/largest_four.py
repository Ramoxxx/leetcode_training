"""
LARGEST FOUR
Pattern: Sorting / select largest elements

Return the sum of the four largest integers in a list. If there are
fewer than four elements, sum all of them. Repeated values count as
separate elements. Negative values count too; do not discard them.

Examples:
    largest_four([4, 5, -2, 3, 1, 2, 6, 6]) -> 21
    largest_four([1, 2, 3]) -> 6
    largest_four([-5, -2, -3, -4, -1]) -> -10

Contract: input is a list of integers. As a local extension, [] returns 0.
Return an integer. Modifying the input is allowed but not required.

Think about: after sorting, which four positions do you need?
Bonus: keep only the four largest values while scanning once.

Source: recueil_questions.md, Coderbyte Largest Four.
"""

from testkit import check, report


def largest_four(nums):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("duplicates count", largest_four([4, 5, -2, 3, 1, 2, 6, 6]), 21)
    check("fewer than four", largest_four([1, 2, 3]), 6)
    check("exactly four", largest_four([9, 1, 2, 3]), 15)
    check("all negative", largest_four([-5, -2, -3, -4, -1]), -10)
    check("must include negative values", largest_four([5, -1, -2, -3, -4]), -1)
    check("not distinct values", largest_four([7, 7, 7, 7, 1]), 28)
    check("single negative", largest_four([-8]), -8)
    check("zeros", largest_four([0, 0, 0, 0, 0]), 0)
    check("empty extension", largest_four([]), 0)
    report()
