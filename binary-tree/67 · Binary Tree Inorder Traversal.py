from typing import (
    List,
)
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

# divide and conquer
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left = self.inorder_traversal(root.left)
        right = self.inorder_traversal(root.right)

        return left + [root.val] + right
    

# dfs
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        res = []

        self.dfs(root, res)

        return res
    
    def dfs(self, root, res):
        if not root:
            return
        
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)



# 中序遍历的非递归写法，出栈以后再访问
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            res.append(root.val)

            if root.right:
                root = root.right
                continue
            
            root = None
        
        return res
    

# 中序遍历的非递归写法
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        dummy = TreeNode(None)
        dummy.right = root
        res = []
        stack = [dummy]

        while stack:
            root = stack.pop()
            if root.right:
                root = root.right
                while root:
                    stack.append(root)
                    root = root.left
            if stack:
                res.append(stack[-1].val)
        
        return res
