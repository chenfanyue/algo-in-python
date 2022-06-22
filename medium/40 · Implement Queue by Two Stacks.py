class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.in_stack = []
        self.out_stack = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.in_stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if not self.out_stack:
            self.transfer()
        
        return self.out_stack.pop()

    """
    @return: An integer
    """
    def top(self):
        if not self.out_stack:
            self.transfer()
        
        return self.out_stack[-1]
    
    def transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
