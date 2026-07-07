class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        for char in t:
            hash_map[char] = hash_map.get(char, 0) - 1

        for count in hash_map.values():
            if count != 0:
                return False

        return True
        