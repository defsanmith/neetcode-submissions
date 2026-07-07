class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i]

        suff[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]

        result = []
        for i in range(n):
            if i == 0:
                result.append(suff[i+1])
            elif i == n - 1:
                result.append(pref[i-1])
            else:
                result.append(pref[i-1] * suff[i+1])

        return result
        