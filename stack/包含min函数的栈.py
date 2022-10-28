# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            last_min = min(self.min_stack[-1], x)
            self.min_stack.append(last_min)

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.data.append(x)

    def pop(self) -> None:
        if self.data:
            value = self.data.pop()
            if value == self.min_stack[-1]:
                del self.min_stack[-1]

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
