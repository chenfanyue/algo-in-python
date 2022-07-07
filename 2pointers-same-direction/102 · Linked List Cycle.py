"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# with the help of hash set
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        visited = set()
        
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False


# use 2pointers
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
