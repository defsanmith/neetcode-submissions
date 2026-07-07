from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = defaultdict(int)
        result = 0

        unq_nums = set(nums)

        for num in nums:
            if num - 1 not in unq_nums:
                curr_num = num
                curr_count = 1
                while curr_num + 1 in unq_nums:
                    curr_num += 1
                    curr_count += 1

                result = max(curr_count, result)


        return result