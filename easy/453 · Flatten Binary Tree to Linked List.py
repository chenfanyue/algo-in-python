from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        self.flatten_and_return_last_node(root)
        
    # restructure and return last node in preorder
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None
            
        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)
        
        # connect 
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        return right_last or left_last or root


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        prelist = list()
        
        def preorder_traverse(root):
            if root:
                prelist.append(root)
                preorder_traverse(root.left)
                preorder_traverse(root.right)

        preorder_traverse(root)
        size = len(prelist)
        for i in range(1, size):
            prev, cur = prelist[i - 1], prelist[i]
            prev.right = cur
            prev.left = None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        prelist = list()
        stack = []
        node = root
        
        while stack or node:
            while node:
                prelist.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(prelist)
        for i in range(1, size):
            prev, cur = prelist[i - 1], prelist[i]
            prev.right = cur
            prev.left = None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            cur = stack.pop()
            if prev:
                prev.left = None
                prev.right = cur
            right, left = cur.right, cur.left
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = cur


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        # write your code here
        cur = root
        while cur:
            if cur.left:
                predecessor = nxt = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right


