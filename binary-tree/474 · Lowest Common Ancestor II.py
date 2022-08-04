"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, a, b):
        if not root or not a or not b:
            return None

        s = set()
        while a:
            s.add(a)
            a = a.parent

        while b:
            if b in s:
                return b
            b = b.parent

        return None
