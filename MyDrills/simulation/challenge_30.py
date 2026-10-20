"""
CHALLENGE 30

A gamified app marks a starting number as "lucky" using this process:
replace the number by the sum of the squares of its digits, and repeat.
If the process eventually reaches 1, the number is lucky. If it instead
loops forever without reaching 1, it is not.

Given a positive integer, return True if it is lucky, otherwise False.

Examples:
    is_lucky(19) -> True   (1+81=82, 64+4=68, 36+64=100, 1+0+0=1)
    is_lucky(2)  -> False

Contract:
n is an integer greater than 0. Return a bool.

"""

from testkit import check, report


def is_lucky(n):
    # TODO: implement
    pass


if __name__ == "__main__":
    check("classic lucky", is_lucky(19), True)
    check("loops forever", is_lucky(2), False)
    check("already one", is_lucky(1), True)
    check("seven is lucky", is_lucky(7), True)
    check("four is not", is_lucky(4), False)
    check("hundred is lucky", is_lucky(100), True)
    check('ends in zero', is_lucky(10), True)
    report()
