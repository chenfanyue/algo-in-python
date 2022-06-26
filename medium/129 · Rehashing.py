"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        capacity = len(hashTable) * 2
        table = [None] * capacity

        for addr in hashTable:
            if addr:
                head = addr
                self.move_to_table(head, table)
            addr = None
        
        del hashTable
        
        return table
    
    def move_to_table(self, head, table):
        capacity = len(table)
        while head:
            cut = head
            head = head.next
            index = self.hashcode(cut.val, capacity)
            cut.next = table[index]
            table[index] = cut
    
    def hashcode(self, key, capacity):
        return key % capacity

