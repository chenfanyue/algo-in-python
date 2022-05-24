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
    @param val: An integer.
    @return: a linked node or null.
    """
    def find_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        while head and head.val != val:
            head = head.next
        
        if head is None:
            return None
        return head


class Solution:
    """
    @param head: the head of linked list.
    @param val: An integer.
    @return: a linked node or null.
    """
    def find_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        while head:
            if head.val == val:
                return head
            head = head.next

        return None


class Solution:
    """
    @param head: the head of linked list.
    @param val: An integer.
    @return: a linked node or null.
    """
    def find_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        while True:
            if head is None:
                return None
            if head.val == val:
                return head
            head = head.next

