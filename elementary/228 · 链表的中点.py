from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        
        p = head
        n = -1
        while p:
            n += 1
            p = p.next
        
        p = head
        n //= 2
        while n > 0:
            p = p.next
            n -= 1
        
        return p


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        
        p = head
        n = -1
        while p:
            n += 1
            p = p.next
        
        p = head
        n //= 2
        for _ in range(n):
            p = p.next
        
        return p


# 数组记录节点地址
class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        
        arr = []
        p = head
        while p:
            arr.append(p)
            p = p.next
        
        return arr[(len(arr) - 1) // 2]


# fast and slow pointers with dummy node
class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head

        dummy = ListNode(0, head)
        fast = slow = dummy

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next is None:
            return slow
        return slow.next


# fast and slow pointers without dummy node
class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middle_node(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
