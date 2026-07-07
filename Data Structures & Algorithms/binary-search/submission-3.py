class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            k = nums[index]
            if k == target:
                return index
            elif k < target:
                left = index + 1
            else:
                right = index - 1

        return -1
            