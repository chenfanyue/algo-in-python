"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# divide and conquer
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        if node.val < root.val:
            left = self.insertNode(root.left, node)
            root.left = left
        elif node.val > root.val:
            right = self.insertNode(root.right, node)
            root.right = right
        
        return root


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        last, cur = None, root

        while cur:
            if node.val < cur.val:
                last, cur = cur, cur.left
            else:
                last, cur = cur, cur.right

        if node.val < last.val:
            last.left = node
        else:
            last.right = node
        
        return root


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if not root:
            return node

        parent, cur = None, root
        left_child = True

        while cur:
            if node.val < cur.val:
                parent, cur = cur, cur.left
                left_child = True
            else:
                parent, cur = cur, cur.right
                left_child = False

        if left_child:
            parent.left = node
        else:
            parent.right = node
        
        return root
