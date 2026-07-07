class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                start = stack.pop()
                if brackets[start] != c:
                    return False

        return True if not stack else False