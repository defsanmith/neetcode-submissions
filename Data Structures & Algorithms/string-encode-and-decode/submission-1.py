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
            len_str = 0
            while(s[i] != '#'):
                len_str = len_str * 10 + int(s[i])
                i += 1

            i += 1
            result.append(s[i:i+len_str])

            i += len_str

        return result
