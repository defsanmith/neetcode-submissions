class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        suffix = [0] * (n + 1)
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i + 1])
        
        area = [0] * n
        for i in range(n):
            area[i] = max(0, min(prefix[i], suffix[i]) - height[i])

        return sum(area)
