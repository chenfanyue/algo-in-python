"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
"""

# bfs
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            n = len(q)
            head = tail = None
            for _ in range(n):
                root = q.popleft()
                node = ListNode(root.val)
                if head is None:
                    tail = head = node
                else:
                    tail.next = node
                    tail = tail.next
                
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(head)
        
        return res


# bfs, 从右往左，链表采用头部插入法
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []

        q = collections.deque([root])
        res = []
        depth = 0

        while q:
            n = len(q)
            depth += 1
            for _ in range(n):
                root = q.popleft()
                node = ListNode(root.val)
                if depth > len(res):
                    res.append(node)
                else:
                    node.next = res[depth - 1]
                    res[depth - 1] = node
                
                if root.right:
                    q.append(root.right)
                if root.left:
                    q.append(root.left)
        
        return res


# dfs, 先遍历右子树，链表采用头部插入法
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        res = []
        self.dfs(root, 1, res)

        return res

    def dfs(self, root, depth, res):
        if not root:
            return

        node = ListNode(root.val)
        if depth > len(res):
            res.append(node)
        else:
            node.next = res[depth - 1]
            res[depth - 1] = node

        self.dfs(root.right, depth + 1, res)
        self.dfs(root.left, depth + 1, res)

