"""
CHALLENGE 7

A gift-card checkout lets a customer combine exactly two products whose
prices add up to the full balance on their card, leaving nothing unspent.
Given the list of product prices (in order on the page) and the card
balance, return the indices of the two products that sum to the balance.

Return the two indices as a list [i, j] with i < j. There is at most one
valid pair; if no pair works, return an empty list.

Examples:
    pair_for_total([2, 7, 11, 15], 9) -> [0, 1]
    pair_for_total([3, 2, 4], 6)      -> [1, 2]

Contract:
Prices and balance are integers. Each index can be used at most once.
Indices start at 0; empty lists are allowed.

"""

from testkit import check, report


def pair_for_total(prices, balance):
    for i in range(0,len(prices)):
        left_val = prices[i]
        left_i = i + 1
        right_i = len(prices) - 1
        while left_i <= right_i:
            mid = (left_i + right_i) // 2
            right_val = prices[mid]
            c_sum = left_val + right_val
            if balance < c_sum:
                right_i = mid - 1
            elif balance > c_sum:
                left_i = mid + 1
            else:
                result = [i,mid]
                result.sort()
                return result
    return []
        
        


if __name__ == "__main__":
    check("basic pair", pair_for_total([2, 7, 11, 15], 9), [0, 1])
    check("pair later", pair_for_total([3, 2, 4], 6), [1, 2])
    check("equal values", pair_for_total([3, 3], 6), [0, 1])
    check("pair at ends", pair_for_total([1, 5, 3, 8], 11), [2, 3])
    check("no pair", pair_for_total([1, 2, 3], 100), [])
    check("single product", pair_for_total([5], 5), [])
    check("empty catalog", pair_for_total([], 0), [])
    check('cannot reuse index', pair_for_total([3, 4], 6), [])
    check('negative values', pair_for_total([-3, 4, 0], 1), [0, 1])
    check('two zeros', pair_for_total([0, 0], 0), [0, 1])
    report()
