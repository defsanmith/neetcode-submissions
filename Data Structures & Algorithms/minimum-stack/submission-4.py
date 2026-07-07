class MinStack:

    def __init__(self):
        self.stack = []
        self._min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self._min = val
        else:
            self.stack.append(val - self._min)
            if val < self._min:
                self._min = val

    def pop(self) -> None:
        top = self.stack.pop()
        if top < 0:
            self._min = self._min - top
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self._min
        
        return self._min
        

    def getMin(self) -> int:
        return self._min
        
