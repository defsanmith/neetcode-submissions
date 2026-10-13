class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, n in enumerate(nums):
            if n in targets:
                return [targets[n], i]

            targets[target - n] = i