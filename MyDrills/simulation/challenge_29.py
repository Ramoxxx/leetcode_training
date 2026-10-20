"""
CHALLENGE 29

A counter device stores a large number as a list of its decimal digits,
most significant digit first (so [1, 2, 3] means 123). The device ticks
up by one. Return the new list of digits after adding one, handling any
carry that ripples through.

Examples:
    tick([1, 2, 3]) -> [1, 2, 4]
    tick([9, 9, 9]) -> [1, 0, 0, 0]

Contract:
The digit list is non-empty. Each digit is an integer from 0 to 9;
there are no leading zeros except for [0]. Return a list of integers.
Modifying the input is allowed but not required.

"""

from testkit import check, report


def tick(digits):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("no carry", tick([1, 2, 3]), [1, 2, 4])
    check("longer input without carry", tick([4, 3, 2, 1]), [4, 3, 2, 2])
    check("single nine", tick([9]), [1, 0])
    check("all nines", tick([9, 9, 9]), [1, 0, 0, 0])
    check("partial carry", tick([1, 9, 9]), [2, 0, 0])
    check("single zero", tick([0]), [1])
    check('internal nines unchanged', tick([9, 0, 9]), [9, 1, 0])
    report()
