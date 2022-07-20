"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        def dfs(root):
            nonlocal last
            if not root:
                return

            dfs(root.left)

            last.right = root
            root.left = last
            last = root
            
            dfs(root.right)
        
        if not root:
            return None

        last = dummy = TreeNode(0)
        dfs(root)
        
        first = dummy.right
        first.left = last
        last.right = first

        return first
        
        
class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if not root:
            return None

        head, tail = self.dfs(root)
        
        head.left = tail
        tail.right = head

        return head
        
    def dfs(self, root):
        # if not root:
        #     return None, None
        if not root.left and not root.right:
            return root, root
        
        if not root.right:
            left_head, left_tail = self.dfs(root.left)
            left_tail.right = root
            root.left = left_tail
            return left_head, root
        
        if not root.left:
            right_head, right_tail = self.dfs(root.right)
            root.right = right_head
            right_head.left = root
            return root, right_tail

        left_head, left_tail = self.dfs(root.left)
        right_head, right_tail = self.dfs(root.right)

        left_tail.right = root
        root.left = left_tail

        root.right = right_head
        right_head.left = root

        return left_head, right_tail


# not recommended
class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        def dfs(root):
            nonlocal first, last
            if not root:
                return

            dfs(root.left)

            if last:
                last.right = root
                root.left = last
            else:
                first = root
            last = root
            
            dfs(root.right)
        
        if not root:
            return None

        first, last = None, None
        dfs(root)
        
        first.left = last
        last.right = first

        return first
        
        
class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        last = dummy = TreeNode(0)
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            last.right = root
            root.left = last
            last = root

            if root.right:
                root = root.right
                continue

            root = None

        first = dummy.right
        first.left = last
        last.right = first

        return first
