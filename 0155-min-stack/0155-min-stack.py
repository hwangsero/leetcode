class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_val = val
        if self.stack:
            min_val = min(self.getMin(), min_val)
        self.stack.append((val, min_val))
        
    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
