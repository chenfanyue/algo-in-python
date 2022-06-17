from typing import (
    List,
)
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
    @return: An integer list
    """
    def to_array_list(self, head: ListNode) -> List[int]:
        # write your code here
        res = []
        while head:
        # while head is not None:
            res.append(head.val)
            head = head.next
        return res


class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """
    def to_array_list(self, head: ListNode) -> List[int]:
        # write your code here
        dummy = ListNode(0, head)
        res = []
        while dummy.next:
            res.append(dummy.next.val)
            dummy = dummy.next
        return res
