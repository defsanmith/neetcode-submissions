class Solution:
    def minWindow(self, s: str, t: str) -> str:
        x, y = 0, 0

        t_counts = Counter(t)
        have, need = 0, len(t_counts)
        window_counts = defaultdict(int)
        l = 0
        min_length = float("inf")
        for r in range(len(s)):
            char = s[r]

            window_counts[char] += 1
            if window_counts[char] == t_counts[char]:
                have += 1

            while l <= r and have == need:
                if r - l + 1 < min_length:
                    x, y = l, r
                    min_length = r - l + 1
                
                window_counts[s[l]] -= 1
                if window_counts[s[l]] < t_counts[s[l]]:
                    have -= 1

                l += 1

        return s[x: y + 1] if min_length != float("inf") else ""