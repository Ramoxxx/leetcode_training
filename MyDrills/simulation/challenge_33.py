"""
CHALLENGE 33

A release pipeline built versions 1 to n in order. At some point a bad
change was introduced, and every version from that one onward is broken.
You are given n and a checker `is_broken(version)` that returns True if a
version is broken. Find and return the first broken version, calling the
checker as few times as you can.

The checker is passed in as a function, so you can call is_broken(v) for
any version v from 1 to n.

Examples:
    first_broken(5, is_broken)  where versions 4 and 5 are broken -> 4
    first_broken(10, is_broken) where only version 10 is broken   -> 10

Contract:
n >= 1, and at least one version is broken. Only query versions in
[1, n]. Use O(log n) checker calls; the tests enforce a call budget.

"""

from testkit import check, report


def first_broken(n, is_broken):    
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if is_broken(mid):
            right = mid
        else:
            left = mid + 1
    return left


   


if __name__ == "__main__":
    check("middle version", first_broken(5, lambda v: v >= 4), 4)
    check("first is broken", first_broken(10, lambda v: v >= 1), 1)
    check("only last broken", first_broken(10, lambda v: v >= 10), 10)
    check("single version", first_broken(1, lambda v: v >= 1), 1)
    check("large range", first_broken(100, lambda v: v >= 37), 37)
    check("five of seven", first_broken(7, lambda v: v >= 5), 5)
    n = 10**9
    calls = [0]

    def bounded_checker(version):
        if type(version) is not int or not 1 <= version <= n:
            raise AssertionError("only integer versions in [1, n] may be queried")
        calls[0] += 1
        if calls[0] > n.bit_length():
            raise AssertionError("too many checker calls: use O(log n) calls")
        return version >= 765432101

    check("large range with call budget", first_broken(n, bounded_checker), 765432101)
    check("logarithmic call count", calls[0] <= n.bit_length(), True)
    report()
