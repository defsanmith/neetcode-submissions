class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            rate = (left + right) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / rate)

            if totalTime <= h:
                result = rate
                right = rate - 1
            else:
                left = rate + 1

        return result