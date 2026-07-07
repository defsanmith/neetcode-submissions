from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord('a') - ord(c)] += 1

            groups[tuple(chars)].append(s)

        return [v for v in groups.values()]

            