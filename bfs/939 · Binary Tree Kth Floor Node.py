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
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloor_node(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0

        q = collections.deque([root])
        depth = 0

        while q:
            depth += 1
            n = len(q)
            if depth == k:
                return n

            for _ in range(n):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        
        return -1
