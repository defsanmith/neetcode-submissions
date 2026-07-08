class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        left, result = 0, 0
        for right in range(len(s)):
            while left < right and s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            result = max(result, right - left + 1)

    
        return result