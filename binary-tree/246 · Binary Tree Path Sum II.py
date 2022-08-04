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

class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum2(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        path = []

        self.dfs(root, target, path, res)

        return res

    def dfs(self, root, target, path, res):
        if not root:
            return
        
        path.append(root.val)
        n = len(path)
        tmp = target
        for i in range(n - 1, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                res.append(path[i:])

        self.dfs(root.left, target, path, res)
        self.dfs(root.right, target, path, res)
        path.pop()
