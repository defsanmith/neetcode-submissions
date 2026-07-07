class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        memo = {}

        result = 0
        for n in nums:
            if n not in numSet:
                continue

            length = 1
            while n + length in numSet:
                length += 1

            current_length = length + memo.get(n + length, 0)
            memo[n] = current_length
                
            result = max(result, current_length)

        return result


