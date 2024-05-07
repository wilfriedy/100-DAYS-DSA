class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            if val < self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1] if self.min else []


solution = MinStack()
solution.push()
solution.push(0)
solution.push(-3)

solution.pop()
solution.pop()
solution.pop()
print(solution.min)
print(solution.stack)