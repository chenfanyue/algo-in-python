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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        arr = []
        self.in_dfs(root, arr)
        return arr[k - 1]

    def in_dfs(self, root: TreeNode, arr = []):
        if root is None:
            return
        
        self.in_dfs(root.left, arr)
        arr.append(root.val)
        self.in_dfs(root.right, arr)


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        arr = [k, [0, 0]]
        self.in_dfs(root, arr)
        return arr[1][1]

    def in_dfs(self, root: TreeNode, arr = []):
        if root is None:
            return

        self.in_dfs(root.left, arr)
        if arr[1][0] == arr[0]:
            return

        arr[1][0] += 1
        arr[1][1] = root.val
        if arr[1][0] == arr[0]:
            return

        self.in_dfs(root.right, arr)


