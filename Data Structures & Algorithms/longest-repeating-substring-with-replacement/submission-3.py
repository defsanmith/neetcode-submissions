class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        counts = defaultdict(int)
        l = 0
        max_count = 0
        for r, c in enumerate(s):
            counts[c] += 1
            max_count = max(max_count, counts[c])

            if r - l - max_count + 1 > k:
                counts[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)


        return result