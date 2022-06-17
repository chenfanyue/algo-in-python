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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        pre = dummy = ListNode(0, head)

        while head:
            if head.val == val:
                pre.next = head.next
                head = pre.next
            else:
                pre = head
                head = head.next
        
        return dummy.next


# time/space both bad
class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        p = dummy = ListNode(0, head)

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        
        return dummy.next
