class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 1:
            return 0

        result = 0
        i, j = 0, 1
        while j < n:
            if prices[i] > prices[j]:
                i = j
            else:
                result = max(result, prices[j] - prices[i])
            j += 1

        return result