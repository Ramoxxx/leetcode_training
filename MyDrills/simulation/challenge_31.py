"""
CHALLENGE 31

A storage allocator only accepts buffer sizes that are an exact power of
two (1, 2, 4, 8, 16, ...). Given a requested size, return True if it is a
power of two, otherwise False. Sizes of zero or below are never valid.

Examples:
    is_power_of_two(16) -> True
    is_power_of_two(3)  -> False

Contract:
Input is an integer (including negative values). Return a bool.

"""

from testkit import check, report


def is_power_of_two(n):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("one", is_power_of_two(1), True)
    check("sixteen", is_power_of_two(16), True)
    check("three", is_power_of_two(3), False)
    check("zero", is_power_of_two(0), False)
    check("negative", is_power_of_two(-4), False)
    check("large power", is_power_of_two(1024), True)
    check("six", is_power_of_two(6), False)
    check('large near miss', is_power_of_two(2**60 + 1), False)
    report()
