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
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insert_node(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        p = dummy = ListNode(0, head)
        
        while p.next and val > p.next.val:
            p = p.next

        node = ListNode(val, p.next)
        p.next = node
        
        return dummy.next
