class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = float('inf')
        for n in prices:
            result = max(result, n - min_price)
            min_price = min(n, min_price)

        return result