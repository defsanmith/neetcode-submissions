class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            a = nums[i]
            while j < k:
                b = nums[j]
                c = nums[k]
                current_sum = a + b + c
                if current_sum == 0:
                    result.append([a, b, c])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif current_sum > 0:
                    k -= 1
                else:
                    j += 1

        return result