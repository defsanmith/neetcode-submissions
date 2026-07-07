class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        n = len(height)
        max_lefts = [0] * n
        max_rights = [0] * n

        max_lefts[0] = height[0]
        for i in range(1, n):
            max_lefts[i] = max(max_lefts[i - 1], height[i])

        max_rights[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], height[i])

        areas = [0] * n
        for i in range(n):
            areas[i] = max(0, min(max_lefts[i], max_rights[i]) - height[i])

        return sum(areas)
        

        