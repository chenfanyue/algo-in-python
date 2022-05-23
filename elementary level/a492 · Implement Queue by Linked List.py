# 描述
# 按链表实现队列。支持以下基本方法：
# enqueue(item).将新元素放入队列中。
# dequeue(). 将第一个元素移出队列，返回它。如果队列为空，则返回-1

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.dummy = LinkedListNode(-1)
        self.tail = self.dummy

    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        new_node = LinkedListNode(item)
        self.tail.next = new_node
        self.tail = new_node

    """
    @return: An integer
    """
    def dequeue(self):
        if self.dummy.next is None:
            return -1
        if self.dummy.next is self.tail:
            self.tail = self.dummy
        ret = self.dummy.next.val
        self.dummy.next = self.dummy.next.next
        return ret
