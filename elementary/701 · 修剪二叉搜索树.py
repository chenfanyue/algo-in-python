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
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        # write your code here
        if root is None:
            return
        
        if root.val > maximum:
            return self.trim_b_s_t(root.left, minimum, maximum)
        
        elif minimum <= root.val <= maximum:
            root.left = self.trim_b_s_t(root.left, minimum, maximum)
            root.right = self.trim_b_s_t(root.right, minimum, maximum)
            return root
        
        else:
            return self.trim_b_s_t(root.right, minimum, maximum)


表面上缩减区间，好像减少查找范围能加快执行。但实际上，对比较判断执行时间相同，反而因为要到堆空间读取root.val加大时间消耗。
class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        # write your code here
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
