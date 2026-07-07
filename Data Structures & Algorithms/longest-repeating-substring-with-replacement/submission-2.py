from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)

        l, result, max_count = 0, 0, 0
        for r in range(len(s)):
            char = s[r]
            char_counts[char] += 1
            max_count = max(max_count, char_counts[char])

            if r - l - max_count + 1 > k:
                char_counts[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)

            
    
        return result
        