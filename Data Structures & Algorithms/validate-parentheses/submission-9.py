class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in mapper:
                stack.append(c)
            elif stack and mapper[stack[-1]] == c:
                stack.pop()
            else:
                return False

        return len(stack) == 0