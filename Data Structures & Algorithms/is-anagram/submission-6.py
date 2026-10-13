class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        for cs in s:
            s_count[ord(cs) - ord('a')] += 1

        for ct in t:
            t_count[ord(ct) - ord('a')] += 1

        for ns, nt in zip(s_count, t_count):
            if ns != nt:
                return False

        return True