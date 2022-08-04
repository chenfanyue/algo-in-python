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
    @return: a ListNode
    """
    def swap_pairs(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        suffix = self.swap_pairs(second.next)

        second.next = first
        first.next = suffix
        return second


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swap_pairs(self, head: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        tail.next = head
        return self.swap_pairs_helper(head, dummy, tail)

    def swap_pairs_helper(self, head, dummy, tail):
        if head is None or head.next is None:
            return dummy.next
        first = head
        second = head.next
        tail.next = second
        first.next = second.next
        second.next = first

        tail = first
        return self.swap_pairs_helper(tail.next, dummy, tail)


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swap_pairs(self, head: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        tail.next = head
        while head and head.next:
            first = head
            second = head.next
            head = second.next
            tail.next = second
            second.next = first
            first.next = head
            tail = first
        return dummy.next


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swap_pairs(self, head: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        tail.next = head
        while head and head.next:
            first = head
            second = head.next
            tail.next = second
            first.next = second.next
            second.next = first

            tail = first
            head = tail.next
        return dummy.next

