"""
CHALLENGE 6

A sensor logs a reading every time a door opens and again when it
closes, so each reading value should appear an even number of times.
Due to one missed event, exactly one value appears an odd number of
times (specifically, every value appears twice except one that appears
once). Return the value that appears only once.

Examples:
    odd_one_out([10, 10, 7])          -> 7
    odd_one_out([3, 5, 3, 5, 8])      -> 8

Contract:
The list is non-empty and contains integers. The frequency rule above
is guaranteed; inputs violating it are out of scope.

"""

from testkit import check, report


def odd_one_out(readings):
    result = 0
    for reading in readings:
        result ^= reading
    return result
    # seen = set()
    # for reading in readings:
    #     if reading in seen:
    #         seen.remove(reading)
    #     else:
    #         seen.add(reading)
    # return next(iter(seen))


if __name__ == "__main__":
    check("odd at end", odd_one_out([10, 10, 7]), 7)
    check("odd in middle", odd_one_out([3, 5, 3, 5, 8]), 8)
    check("single reading", odd_one_out([42]), 42)
    check("with zero", odd_one_out([0, 1, 1]), 0)
    check("odd at start", odd_one_out([8, 3, 3, 5, 5]), 8)
    check("negative value", odd_one_out([-2, 4, 4]), -2)
    check('single zero', odd_one_out([0]), 0)
    report()
