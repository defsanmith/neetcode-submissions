class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        result = 0
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            result = max(result, area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return result
        