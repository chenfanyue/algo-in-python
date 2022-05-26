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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        after = dummy = ListNode(0, head)

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            after = after.next
        
        after.next = after.next.next

        return dummy.next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        p = dummy = ListNode(0, head)

        for _ in range(self.getLength(head) - n):
            p = p.next
        
        p.next = p.next.next

        return dummy.next

    def getLength(self, head: ListNode) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res


# not fast enough, dont let ahead stop at the last real node
# instead the null node
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        after = ahead = dummy = ListNode(0, head)

        for _ in range(n):
            ahead = ahead.next
        
        while ahead.next:
            ahead = ahead.next
            after = after.next
        
        after.next = after.next.next

        return dummy.next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        def getLength(head: ListNode) -> int:
            res = 0
            while head:
                res += 1
                head = head.next
            return res
        
        p = dummy = ListNode(0, head)

        for _ in range(getLength(head) - n):
            p = p.next
        
        p.next = p.next.next

        return dummy.next
