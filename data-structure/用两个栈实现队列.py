# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

class CQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        if len(self.outStack) == 0:
            if len(self.inStack) == 0:
                return -1
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()


class CQueue:

    def __init__(self):
        self.que = deque()

    def appendTail(self, value: int) -> None:
        self.que.append(value)

    def deleteHead(self) -> int:
        if len(self.que) == 0:
            return -1
        return self.que.popleft()
            

class CQueue:

    def __init__(self):
        self.que = []

    def appendTail(self, value: int) -> None:
        self.que.append(value)

    def deleteHead(self) -> int:
        if len(self.que) == 0:
            return -1
        return self.que.pop(0)


# 滥用异常
class CQueue:

    def __init__(self):
        self.que = []

    def appendTail(self, value: int) -> None:
        self.que.append(value)

    def deleteHead(self) -> int:
        try:
            return self.que.pop(0)
        except:
            return -1


