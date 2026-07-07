class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}

        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1

        for char in t:
            hashMap[char] = hashMap.get(char, 0) - 1

        for count in hashMap.values():
            if count != 0:
                return False
                
        return True
        