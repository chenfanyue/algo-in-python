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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
            
        res = []
        self.dfs(root, [], res)
        
        return res

    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            path.append(root)
            res.append(list(path))
            path.pop()
            return
        
        path.append(root)
        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)
        path.pop()

