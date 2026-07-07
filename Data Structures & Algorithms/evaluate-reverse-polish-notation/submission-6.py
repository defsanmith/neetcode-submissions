class Solution:
    def is_number(self, s):
        try:
            int(s)  # Try to convert to float
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if self.is_number(t):
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()

                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))

        return int(stack[-1])