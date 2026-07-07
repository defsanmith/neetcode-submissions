class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        profit = 0
        i, j = 0, 1
        while i < n and j < n:
            while j < n and prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
                j += 1

            i = j
            j += 1

        return profit
        