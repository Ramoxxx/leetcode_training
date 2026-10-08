# TimeoutError 8
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i,price in enumerate(prices):
            for j in range(i+1,len(prices)):
                max_profit = max(prices[j] - price, max_profit)
        return max_profit

        