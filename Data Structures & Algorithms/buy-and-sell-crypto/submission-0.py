class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for idx in range(len(prices) - 1):
            next_max = max(prices[idx + 1:])
            profit = max(profit, next_max - prices[idx])

        return profit