class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in nums_set:
                current = num
                current_streak = 1

                while current + 1 in nums_set:
                    current += 1
                    current_streak += 1

                result = max(result, current_streak)

        return result