class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        profit = 0
        left, right = 0, 1
        while right < n:
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right

            right += 1

        return profit
        