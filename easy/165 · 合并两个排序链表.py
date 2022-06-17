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

# recommended
class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy1 = ListNode(0, l1)
        dummy2 = ListNode(0, l2)
        tail = dummy = ListNode(0)

        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val < l2.val:
                dummy1.next = l1.next
                tail.next = l1
                tail = tail.next
                l1 = dummy1.next
            else:
                dummy2.next = l2.next
                tail.next = l2
                tail = tail.next
                l2 = dummy2.next
        
        return dummy.next


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        tail = dummy = ListNode(0)

        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        
        return dummy.next


# recommended
class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy1 = ListNode(0, l1)
        dummy2 = ListNode(0, l2)
        tail = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                dummy1.next = l1.next
                tail.next = l1
                tail = tail.next
                l1 = dummy1.next
            else:
                dummy2.next = l2.next
                tail.next = l2
                tail = tail.next
                l2 = dummy2.next
        
        # tail.next = l2 if l1 is None else l1
        if l1 is None:
            tail.next = l2
            return dummy.next
        else:
            tail.next = l1
            return dummy.next


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        tail = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        
        # tail.next = l2 if l1 is None else l1
        if l1 is None:
            tail.next = l2
            return dummy.next
        else:
            tail.next = l1
            return dummy.next


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l2.next, l1)
            return l2


# recommended, 带状态量递归
class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        tail = dummy = ListNode(0)
        self.merge_helper(tail, l1, l2)
        return dummy.next

    def merge_helper(self, tail, l1: ListNode, l2: ListNode):
        if l1 is None:
            tail.next = l2
            return

        if l2 is None:
            tail.next = l1
            return

        if l1.val < l2.val:
            tail.next = l1
            tail = tail.next
            self.merge_helper(tail, l1.next, l2)
        else:
            tail.next = l2
            tail = tail.next
            self.merge_helper(tail, l1, l2.next)


# not recommended, 只是演示while True形式的迭代能和尾递归相互转换
class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy1 = ListNode(0, l1)
        dummy2 = ListNode(0, l2)
        tail = dummy = ListNode(0)
        self.merge_helper(tail, dummy1, l1, dummy2, l2)
        return dummy.next

    def merge_helper(self, tail, dummy1: ListNode, l1: ListNode, dummy2: ListNode, l2: ListNode):
        if l1 is None:
            tail.next = l2
            return

        if l2 is None:
            tail.next = l1
            return

        if l1.val < l2.val:
            dummy1.next = l1.next
            tail.next = l1
            tail = tail.next
            l1 = dummy1.next
            self.merge_helper(tail, dummy1, l1, dummy2, l2)
        else:
            dummy2.next = l2.next
            tail.next = l2
            tail = tail.next
            l2 = dummy2.next
            self.merge_helper(tail, dummy1, l1, dummy2, l2)
