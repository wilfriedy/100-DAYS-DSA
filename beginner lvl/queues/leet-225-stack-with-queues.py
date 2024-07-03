from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        self.queue.extendleft([x])
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:

    def empty(self) -> bool:
        pass