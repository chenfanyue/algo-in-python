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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        less, larger = -float('inf'), float('inf')

        while root:
            if root.val == target:
                return root.val
            elif root.val < target:
                less = root.val
                root = root.right
            else:
                larger = root.val
                root = root.left
        
        if target - less < larger - target:
            return int(less)
        return int(larger)


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        less, larger = -float('inf'), float('inf')

        return self.helper(root, target, less, larger)

    def helper(self, root, target, less, larger):
        if not root:
            return int(less) if target - less < larger - target else int(larger)
        
        if root.val == target:
            return root.val
        elif root.val < target:
            less = root.val
            return self.helper(root.right, target, less, larger)
        else:
            larger = root.val
            return self.helper(root.left, target, less, larger)
