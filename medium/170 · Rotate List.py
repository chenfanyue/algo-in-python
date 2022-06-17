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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if not head:
            return None
        
        addrs = []
        while head:
            addrs.append(head)
            head = head.next
        
        n = len(addrs)
        k %= n

        # if 0 == k:
        #     return addrs[0]
        addrs[-1].next = addrs[0]
        addrs[n - k - 1].next = None

        return addrs[-k]


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if not head:
            return None
        
        p = head
        n = 0
        while p:
            n += 1
            tail = p # suppose current node might be the last real node
            p = p.next
        
        k %= n

        if 0 == k:
            return head
        p = head
        for _ in range(n - k - 1):
            p = p.next

        tail.next = head
        res = p.next
        p.next = None

        return res


# traverse to tail, tail connects to head, tail moves n-k
class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if not head:
            return None
        
        p = head
        n = 0
        while p:
            n += 1
            tail = p # suppose current node might be the last real node
            p = p.next
        
        k %= n

        if 0 == k:
            return head
        
        tail.next = head
        for _ in range(n - k):
            tail = tail.next

        res = tail.next
        tail.next = None

        return res


# not recommended, ahead and after two pointers
class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        if not head:
            return None
        
        p = head
        n = 0
        while p:
            n += 1
            tail = p # suppose current node might be the last real node
            p = p.next
        
        k %= n

        if 0 == k:
            return head
        
        after = ahead = head
        for _ in range(k + 1):
            ahead = ahead.next
        while ahead:
            ahead = ahead.next
            after = after.next

        tail.next = head
        res = after.next
        after.next = None

        return res
