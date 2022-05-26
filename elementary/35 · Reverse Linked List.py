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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        p = head
        # tail will stop at the last real node
        stack = list()
        while p:
            stack.append(p)
            p = p.next
        
        tail = dummy = ListNode(0)
        while stack:
            tail.next = stack.pop()
            tail = tail.next
        tail.next = None
        
        return dummy.next


# the fastest way to build a linked list
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        p = head
        # stack = list()
        # stack.append(None)
        # tail will stop at the last node which is None
        stack = [None]
        while p:
            stack.append(p)
            p = p.next
        
        tail = dummy = ListNode(0)
        while stack:
            tail.next = stack.pop()
            tail = tail.next
        
        return dummy.next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        # null node is the first and only node of a new linked list
        first = None
        
        while head:
            tmp = head
            head = head.next
            tmp.next = first
            first = tmp
        
        return first


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        # dummy = ListNode(0, None)
        dummy = ListNode(0)
        
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        
        return dummy.next


# 分治法递归
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head

        res = self.reverse(head.next)
        # head.next is the last real node of res
        head.next.next = head
        head.next = None # avoid infinite loop

        return res


# 等价转换递归
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        # null node is the first and only node of a new linked list
        return self.reverse_helper(None, head)
    
    # 递归定义，反转head链表，放在first前面得到一个新链表
    def reverse_helper(self, first: ListNode, head: ListNode) -> ListNode:
        if head is None:
            return first
        
        tmp = head
        head = head.next
        tmp.next = first
        first = tmp
        return self.reverse_helper(first, head)
