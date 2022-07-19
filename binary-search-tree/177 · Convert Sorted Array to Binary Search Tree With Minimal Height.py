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
    @param a: an integer array
    @return: A tree node
    """
    def sorted_array_to_b_s_t(self, a: List[int]) -> TreeNode:
        if not a:
            return None

        # left, right = 0, len(a) - 1
        mid = (0 + len(a) - 1) >> 1
        root = TreeNode(a[mid])

        root.left = self.sorted_array_to_b_s_t(a[:mid])
        root.right = self.sorted_array_to_b_s_t(a[mid+1:])

        return root


class Solution:
    """
    @param a: an integer array
    @return: A tree node
    """
    def sorted_array_to_b_s_t(self, a: List[int]) -> TreeNode:
        return self.dfs(a, 0, len(a) - 1)

    def dfs(self, a, start, end):
        if start > end:
            return None
        # if start == end:
        #     return TreeNode(a[start])

        mid = (start + end) >> 1
        root = TreeNode(a[mid])

        root.left = self.dfs(a, start, mid - 1)
        root.right = self.dfs(a, mid + 1, end)

        return root




