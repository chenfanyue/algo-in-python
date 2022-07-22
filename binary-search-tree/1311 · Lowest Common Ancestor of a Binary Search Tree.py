"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        def dac(root):
            nonlocal small, big, p, q
            if not root:
                return None

            if small <= root.val <= big:
                return root
            if root.val < small:
                return dac(root.right)
            return dac(root.left)

        small, big = min(p.val, q.val), max(p.val, q.val)

        return dac(root)
