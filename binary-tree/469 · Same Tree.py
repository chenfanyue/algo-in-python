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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def is_identical(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if (a and not b) or (not a and b):
            return False
        if a and b and (a.val != b.val):
            return False
        
        # a and b and (a.val == b.val):
        # need to compare subtrees
        left = self.is_identical(a.left, b.left)
        right = self.is_identical(a.right, b.right)
        return left and right


# dfs, traverse 2 trees synchronously
class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def is_identical(self, a: TreeNode, b: TreeNode) -> bool:
        res = [True]
        self.dfs(a, b, res)

        return res[0]
    
    def dfs(self, a, b, res):
        if not a and not b:
            return
        if (a and not b) or (not a and b):
            res[0] = False
            return
        if a and b and (a.val != b.val):
            res[0] = False
            return
        # a and b and (a.val == b.val):
        # do nothing
        
        self.dfs(a.left, b.left, res)
        self.dfs(a.right, b.right, res)

