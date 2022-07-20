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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def right_side_view(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque([root])

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return res
