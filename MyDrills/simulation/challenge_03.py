"""
CHALLENGE 3

You are given the price of a product recorded once per day, in order.
You may "buy" on one day and "sell" on a later day. Return the maximum
profit you could have made from a single buy-then-sell. If no profit is
possible, return 0.

You cannot sell before you buy.

Examples:
    best_profit([7, 1, 5, 3, 6, 4]) -> 5    (buy at 1, sell at 6)
    best_profit([7, 6, 4, 3, 1])    -> 0    (prices only fall)

Contract:
Prices are non-negative integers. Fewer than two days returns 0.

"""

from testkit import check, report


def best_profit(prices):
    if len(prices) < 2:
        return 0
    buy_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit,price - buy_price)
        buy_price = min(buy_price,price)
    return max_profit
        
        


if __name__ == "__main__":
    check("profit possible", best_profit([7, 1, 5, 3, 6, 4]), 5)
    check("no profit", best_profit([7, 6, 4, 3, 1]), 0)
    check("flat prices", best_profit([3, 3, 3]), 0)
    check("rising prices", best_profit([1, 2, 3, 4]), 3)
    check("single day", best_profit([5]), 0)
    check("empty", best_profit([]), 0)
    check('cannot sell before buying', best_profit([9, 2, 3]), 1)
    check('two days', best_profit([0, 4]), 4)
    report()
