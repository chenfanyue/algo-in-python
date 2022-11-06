# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        done = None
        while head:
            headNext = head.next
            head.next = done
            done = head
            head = headNext
        return done


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        done = None
        return self.changeState(done, head)

    def changeState(self, done: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return done

        headNext = head.next
        head.next = done
        done = head
        return self.changeState(done, headNext)
