class InterfaceQueue:
    def push(self, element):
        pass

    # define an interface for pop method
    # write your code here
    def pop(self):
        pass

    # define an interface for top method
    # write your code here
    def top(self):
        pass

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.tail = self.dummy = ListNode(0)
		
    # implement the push method
    # write your code here
    def push(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
		
    # implement the pop method
    # write your code here
    def pop(self):
        if self.dummy.next is None:
            return None
        if self.dummy.next == self.tail:
            self.tail = self.dummy
        val = self.dummy.next.val
        self.dummy.next = self.dummy.next.next
        return val
    	
	# implement the top method
    # write your code here
    def top(self):
        if self.dummy.next is None:
            return None
        return self.dummy.next.val


class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.tail = self.head = None
        
    # implement the push method
    # write your code here
    def push(self, val):
        if self.head is None:
            self.tail = self.head = ListNode(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        
    # implement the pop method
    # write your code here
    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            val = self.head.val
            self.tail = self.head = None
            return val
        val = self.head.val
        self.head = self.head.next
        return val
        
    # implement the top method
    # write your code here
    def top(self):
        if self.head is None:
            return None
        return self.head.val


# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue
