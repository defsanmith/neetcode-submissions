class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        char_to_index = lambda char: ord(char) - ord('a')

        for char in s1:
            s1_count[char_to_index(char)] += 1

        for char in s2[:len(s1)]:
            s2_count[char_to_index(char)] += 1

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            s2_count[char_to_index(s2[i])] += 1
            s2_count[char_to_index(s2[i - len(s1)])] -= 1

            if s1_count == s2_count:
                return True

        return False