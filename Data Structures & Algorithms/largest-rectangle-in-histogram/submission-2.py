class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, h_top = stack.pop()
                maxArea = max(maxArea, h_top * (i - start))
            stack.append([start, h])

        end = len(heights)

        while stack:
            start, h_top = stack.pop()
            maxArea = max(maxArea, h_top * (end - start))

        return maxArea