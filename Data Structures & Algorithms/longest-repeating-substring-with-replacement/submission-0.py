class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        max_count = 0
        max_length = 0

        start = 0

        for end in range(len(s)):
            char = s[end]
            freq[char] = freq.get(char, 0) + 1
            max_count = max(max_count, freq[char])

            if (end - start + 1) - max_count > k:
                freq[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

