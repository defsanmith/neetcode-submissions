class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            
            s_len = int(s[start: end])
            start = end + 1
            end = start + s_len
            decoded.append(s[start: end])
            start = end

        return decoded

            
