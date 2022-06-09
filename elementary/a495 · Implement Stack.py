class Stack:
    def __init__(self):
        self.data = []
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.data.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        return self.data.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.data[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.data) == 0


class Stack:
    def __init__(self):
        self.data = collections.deque()
    
    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0
