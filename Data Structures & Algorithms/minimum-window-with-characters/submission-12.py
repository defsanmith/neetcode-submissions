from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if ns < nt:
            return ""
            
        t_count = Counter(t)
        win_count = defaultdict(int)
        min_len = float('inf')
        result = ""
        have, need = 0, len(t_count)
        left = 0
        for right in range(ns):
            char = s[right]
            win_count[char] += 1

            if char in t_count and t_count[char] == win_count[char]:
                have += 1

            while have == need:
                print(left, right)
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left: right + 1]

                win_count[s[left]] -= 1
                if s[left] in t_count and win_count[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1


        return result