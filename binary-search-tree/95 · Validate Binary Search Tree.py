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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        last = -float('inf')
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= last:
                return False
            last = root.val

            if root.right:
                root = root.right
                continue

            root = None

        return True


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        last = -float('inf')
        stack = [(root, 0)]

        while stack:
            root, state = stack.pop()
            if not root:
                continue

            if state == 0:
                stack.extend([
                    (root.right, 0),
                    (root, 3),
                    (root.left, 0)
                ])

            if state == 3:
                if root.val <= last:
                    return False
                last = root.val

        return True

