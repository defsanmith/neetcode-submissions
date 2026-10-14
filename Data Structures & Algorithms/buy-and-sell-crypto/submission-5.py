class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        result = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                result = max(result, prices[j] - prices[i])
            else:
                i = j
        
        return result