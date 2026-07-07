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
            str_len = 0
            while s[i] != '#':
                str_len = str_len * 10 + int(s[i])
                i += 1

            i += 1
            result.append(s[i: i + str_len])

            i += str_len

        return result
