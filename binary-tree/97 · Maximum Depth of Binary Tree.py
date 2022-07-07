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

# dfs
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        res = [0, 0]

        self.dfs(root, res)

        return res[1]
    
    def dfs(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res[0] += 1
            res[1] = max(res[1], res[0])
            res[0] -= 1
            return
        
        res[0] += 1
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res[0] -= 1


# divide and conquer
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.max_depth(root.right) + 1
        if not root.right:
            return self.max_depth(root.left) + 1
        
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        return max(left, right) + 1
