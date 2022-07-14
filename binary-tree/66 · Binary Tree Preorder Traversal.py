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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        left = self.preorder_traversal(root.left)
        right = self.preorder_traversal(root.right)

        return [root.val] + left + right


# dfs
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []

        self.dfs(root, res)

        return res
    
    def dfs(self, root, res):
        if not root:
            return
        
        res.append(root.val)
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)


# 前序遍历非递归的写法，先访问再入栈
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            if root.right:
                root = root.right
                continue
            
            root = None
        
        return res


# 模拟递归调用栈
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(root, 0)]

        while stack:
            root, state = stack.pop()
            if not root:
                continue
            
            if state == 0:
                stack.extend([
                    (root.right, 0),
                    (root.left, 0),
                    (root, 3)
                ])
            
            if state == 3:
                res.append(root.val)
        
        return res


# Morris algo
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []

        while root:
            if root.left:
                probe = root.left
                while probe.right and probe.right != root:
                    probe = probe.right
                
                if not probe.right:
                    res.append(root.val)
                    probe.right = root
                    root = root.left
                else:
                    probe.right = None
                    root = root.right

            else:
                res.append(root.val)
                root = root.right
            
        return res

