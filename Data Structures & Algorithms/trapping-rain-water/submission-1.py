class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        n = len(height)
        max_left, max_right = 0, 0
        left, right = 0, n - 1

        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water