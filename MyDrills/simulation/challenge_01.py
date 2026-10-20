"""
CHALLENGE 1

An online shop generates an order ID for every purchase. Because of a
bug, some IDs may have been issued twice. Given the list of order IDs
recorded today, determine whether the shop issued any ID more than once.

Return True if at least one ID is repeated, False otherwise.

Examples:
    has_repeat([1001, 1002, 1003, 1001]) -> True
    has_repeat([1, 2, 3, 4, 5])          -> False

Contract:
IDs are integers. An empty list returns False.

"""

from testkit import check, report


def has_repeat(order_ids):
    seen = set()
    for id in order_ids:
        if id in seen:
            return True
        seen.add(id)
    return False


if __name__ == "__main__":
    check("a repeat exists", has_repeat([1001, 1002, 1003, 1001]), True)
    check("all unique", has_repeat([1, 2, 3, 4, 5]), False)
    check("empty day", has_repeat([]), False)
    check("one order", has_repeat([42]), False)
    check("repeat far apart", has_repeat([7, 1, 2, 3, 4, 7]), True)
    check('zero duplicate', has_repeat([0, 1, 0]), True)
    report()
