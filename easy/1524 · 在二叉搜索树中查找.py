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

侧重在迭代
分析出迭代的方向和过程，迭代的终点。迭代终点取反得到迭代的前提。
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        while root and root.val != val: #迭代的前提，相反面就是迭代的终点
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root


二分搜索，深度查找
// 实际运行很慢
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None


分治法，递归
T = O(h), h = (logN, N)
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        # Write your code here.
        if root is None:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.search_b_s_t(root.left, val)
        else:
            return self.search_b_s_t(root.right, val)


T = O(n)
可以对任意二叉树遍历查找，实际运行居然比bst还快
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        # Write your code here.
        if root is None or root.val == val:
            return root
        
        res = self.search_b_s_t(root.left, val)
        if res:
            return res
        
        return self.search_b_s_t(root.right, val)
