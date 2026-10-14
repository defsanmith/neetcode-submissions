class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1

        result = 0
        while end < len(prices):
            if prices[end] > prices[start]:
                result = max(result, prices[end] - prices[start])
            else:
                start = end
            
            end += 1

        return result