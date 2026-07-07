class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                int(s)  # Try to convert to float
                return True
            except ValueError:
                return False

        stack = []

        for char in tokens:
            if is_number(char):
                stack.append(int(char))
            else:
                a, b = stack.pop(), stack.pop()

                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(b - a)
                elif char == '*':
                    stack.append(int(a * b))
                elif char == '/':
                    stack.append(int(b / a))
        
        return stack[-1]