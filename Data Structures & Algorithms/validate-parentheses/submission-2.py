class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_brackets:
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
            
        