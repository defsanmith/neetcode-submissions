class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s 

        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            n = 0
            while s[i] != '#':
                n = n * 10 + int(s[i])
                i += 1

            i += 1

            string = ''
            while n > 0:
                string += s[i]
                i += 1
                n -= 1
            
            result.append(string)

        return result

