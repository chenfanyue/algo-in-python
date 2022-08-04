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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                root = q.popleft()
                tmp.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(list(tmp))
        
        res.reverse()

        return res
