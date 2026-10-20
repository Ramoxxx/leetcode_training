"""
CHALLENGE 14

A meter reports temperature readings already sorted in non-decreasing
order, but the log contains consecutive repeats of the same value. The
storage team wants to know how many distinct readings the log holds so
they can size a compacted table.

Given the sorted list, return the count of distinct values.

Examples:
    distinct_count([1, 1, 2])                      -> 2
    distinct_count([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) -> 5

Contract:
Readings are integers. Empty input returns 0. You only need to return
a count; compacting or modifying the list is not required.

"""

from testkit import check, report


def distinct_count(readings):
    return len(set(readings))


if __name__ == "__main__":
    check("one repeat", distinct_count([1, 1, 2]), 2)
    check("many repeats", distinct_count([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
    check("empty log", distinct_count([]), 0)
    check("single reading", distinct_count([1]), 1)
    check("all same", distinct_count([2, 2, 2, 2]), 1)
    check("already distinct", distinct_count([1, 2, 3, 4]), 4)
    check("negative readings", distinct_count([-2, -2, -1, 0, 0]), 3)
    check('all negative duplicates', distinct_count([-3, -3, -2, -2]), 2)
    report()
