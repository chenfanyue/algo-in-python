"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return None
        
        path_a, path_b = [], []
        self.get_path(root, A, path_a)
        self.get_path(root, B, path_b)
        
        a_len, b_len = len(path_a), len(path_b)
        i = 0
        while i < a_len and i < b_len:
            if path_a[i] == path_b[i]:
                i += 1
            else:
                return path_a[i - 1]
        
        if len(path_a) <= len(path_b):
            return path_a[i - 1]
        return path_b[i - 1]

    def get_path(self, root, node, path=[]):
        if not root:
            return
        
        path.append(root)
        if root == node:
            return
        
        self.get_path(root.left, node, path)
        if path[-1] == node:
            return
        
        self.get_path(root.right, node, path)
        if path[-1] == node:
            return

        path.pop()



