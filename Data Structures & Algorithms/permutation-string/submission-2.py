class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for char in s1:
            s1_count[ord(char) - 97] += 1   
        s1_count = tuple(s1_count)
        
        n1 = len(s1)
        n2= len(s2)
        for r in range(n2 - n1 + 1):
            s2_count = [0] * 26
            sub_string = s2[r: r + n1]
            for char in sub_string:
                s2_count[ord(char) - 97] += 1
            print(sub_string, s1_count, s2_count)
            if s1_count == tuple(s2_count):
                return True

        return False