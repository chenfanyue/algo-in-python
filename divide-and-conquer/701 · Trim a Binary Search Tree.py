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
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        if root is None:
            return
        
        if root.val > maximum:
            return self.trim_b_s_t(root.left, minimum, maximum)
        
        elif minimum <= root.val <= maximum:
            root.left = self.trim_b_s_t(root.left, minimum, root.val)
            root.right = self.trim_b_s_t(root.right, root.val, maximum)
            return root
        
        else:
            return self.trim_b_s_t(root.right, minimum, maximum)
