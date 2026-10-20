"""
CHALLENGE 24

A monitoring tool reports the best average load over any window of k
consecutive minutes. Given the per-minute load values and the window
size k, return the highest average of any k consecutive values.

You may assume k is at least 1 and no larger than the number of values.
Return the average as a float.

Examples:
    best_average([1, 12, -5, -6, 50, 3], 4) -> 12.75
    best_average([5], 1)                     -> 5.0

Contract:
Loads are integers and may be negative. Floating-point rounding
differences up to the test helper tolerance are accepted.

"""

from testkit import check, report


def best_average(loads, k):
    current_sum = sum(loads[:k])
    max_sum = current_sum
    for i in range(1,len(loads) - k + 1):
        current_sum += loads[i + k - 1]
        current_sum -= loads[i - 1]
        max_sum = max(max_sum,current_sum)
    return max_sum / k
    


if __name__ == "__main__":
    check("window of four", best_average([1, 12, -5, -6, 50, 3], 4), 12.75)
    check("single value", best_average([5], 1), 5.0)
    check("window of one", best_average([0, 4, 0, 3, 2], 1), 4.0)
    check("all negative", best_average([-1, -2, -3, -4], 2), -1.5)
    check("uniform", best_average([1, 1, 1, 1], 2), 1.0)
    check("whole array", best_average([7, 4, 4], 3), 5.0)
    check('fractional result', best_average([0, 0, 1], 3), 0.3333333333333333)
    check('best window last', best_average([1, 2, 8, 9], 2), 8.5)
    report()
