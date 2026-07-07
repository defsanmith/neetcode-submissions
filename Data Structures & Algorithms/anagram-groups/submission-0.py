from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            charset = [0] * 26
            for c in s:
                charset[ord(c) - 97] += 1

            result[tuple(charset)].append(s)

        return result.values()
