# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head != None:
            res.append(head.val)
            head = head.next

        # return res[::-1]
        # res.reverse()
        l, r = 0, len(res)-1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

        return res
