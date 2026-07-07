from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        win_count = defaultdict(int)

        min_len = float('inf')
        min_substr = ""
        have, need = 0, len(t_count)

        left, right = 0, 0

        while right < len(s):
            char = s[right]
            win_count[char] += 1

            if char in t_count and win_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_substr = s[left: right + 1]

                win_count[s[left]] -= 1
                if s[left] in t_count and win_count[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

            right += 1

        return min_substr

        


        