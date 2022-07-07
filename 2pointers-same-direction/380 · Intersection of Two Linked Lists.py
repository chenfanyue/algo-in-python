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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next
        
        while headB:
            if headB in visited:
                return headB
            headB = headB.next
        
        return None


# 2pointers
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        a = headA
        while headA:
            tail_a = headA
            headA = headA.next

        tail_a.next = headB
        
        slow, fast = a, a.next
        while fast != slow:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        
        while a != slow.next:
            a = a.next
            slow = slow.next
        
        tail_a.next = None
        
        return a
