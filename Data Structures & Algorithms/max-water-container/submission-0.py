class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        result = 0
        while i < j:
            lx = j - i
            ly = min(heights[i], heights[j])

            result = max(result, lx * ly)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1


        return result