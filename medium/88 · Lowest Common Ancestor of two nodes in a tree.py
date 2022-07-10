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

        shorter, longer = path_a, path_b
        if len(path_a) > len(path_b):
            shorter, longer = path_b, path_a
        
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                return shorter[i - 1]
        
        return shorter[-1]
        
        # left, right = 0, len(shorter) - 1
        # idx = -1
        # while left <= right:
        #     mid = (left + right) >> 1
        #     if shorter[mid] == longer[mid]:
        #         idx = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return shorter[idx]


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


# 不理解
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return None
        if root == A or root == B:
            return root
        
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
