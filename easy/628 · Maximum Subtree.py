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
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        max_weight = -float('inf')
        p = None
        res = self.dfs(root, p, max_weight)[1]
        
        return res
    
    def dfs(self, root, p, max_weight):
        if not root:
            return 0, p, max_weight
        
        left_weight, p, max_weight = self.dfs(root.left, p, max_weight)
        right_weight, p, max_weight = self.dfs(root.right, p, max_weight)

        weight = left_weight + right_weight + root.val
        if weight > max_weight:
            max_weight = weight
            p = root
        
        return weight, p, max_weight


class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        subtree = self.dac(root)[1]
        return subtree
    
    def dac(self, root):
        if not root:
            return (-float('inf'), None, 0)
        if not root.left and not root.right:
            return (root.val, root, root.val)
        
        left_max, left_subtree, left_sum = self.dac(root.left)
        right_max, right_subtree, right_sum = self.dac(root.right)
        root_sum = left_sum + right_sum + root.val

        if max(left_max, right_max, root_sum) == left_max:
            return left_max, left_subtree, root_sum
        if max(left_max, right_max, root_sum) == right_max:
            return right_max, right_subtree, root_sum
        return root_sum, root, root_sum

