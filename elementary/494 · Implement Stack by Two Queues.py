class Stack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q2.append(x)
        # while len(self.q1) > 0:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: nothing
    """
    def pop(self):
        return self.q1.popleft()

    """
    @return: An integer
    """
    def top(self):
        return self.q1[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.q1


class Stack:
    def __init__(self):
        self.q = collections.deque()
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        n = len(self.q)
        self.q.append(x)
        for _ in range(n):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.q


class Stack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.q1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

    """
    @return: An integer
    """
    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.q1
