class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = {string: len(string) for string in strs}
        result = []
        for string in strs:
            result.append(str(lengths[string]) + "#")
            result.append(string)
            
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        # 5#Hello5#World
        i = 0
        while i < len(s):
            l = 0
            while s[i] != "#":
                l = l * 10 + int(s[i])
                i += 1
            
            i += 1
            result.append(s[i: i + l])

            i = i + l

        return result
