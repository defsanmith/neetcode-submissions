class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        start, end = 0, len(heights) - 1

        while start < end:
            result = max(result, (end - start) * min(heights[start], heights[end]))

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return result