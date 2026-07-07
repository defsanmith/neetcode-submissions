class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = ''.join(char.lower() for char in s if char.isalnum())

        n = len(sanitized)

        i = 0
        while i < n // 2:
            if sanitized[i] != sanitized[n - i - 1]:
                return False

            i += 1

        return True