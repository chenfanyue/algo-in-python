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

# traverse with carrying states
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        return self.find_min_tree(root, None, float('inf'))[0]

    def find_min_tree(self, root, least_tree, least):
        if not root:
            return least_tree, least, 0
        
        least_tree, least, left_sum = self.find_min_tree(root.left, least_tree, least)
        least_tree, least, right_sum = self.find_min_tree(root.right, least_tree, least)
        total_sum = left_sum + right_sum + root.val
        if total_sum < least:
            least = total_sum
            least_tree = root
        
        return least_tree, least, total_sum


# divide and conquer

