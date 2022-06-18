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

# inorder dfs and traverse with states
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


# inorder dfs using iteration with register group
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        stack = []
        cnt, val = 0, 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            cnt, val = cnt + 1, root.val
            if cnt == k:
                return val
            root = root.right


# 附加节点个数计数器, then quick select
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        nodes_cnt = dict()
        self.build_nodes_cnt(root, nodes_cnt)
        return self.get_kth(root, k, nodes_cnt)

    def build_nodes_cnt(self, root, nodes_cnt):
        if not root:
            return 0
        
        left = self.build_nodes_cnt(root.left, nodes_cnt)
        right = self.build_nodes_cnt(root.right, nodes_cnt)
        total = left + right + 1
        nodes_cnt[root] = total

        return total
    
    def get_kth(self, root, k, nodes_cnt):
        left = nodes_cnt[root.left] if root.left else 0

        if k <= left:
            return self.get_kth(root.left, k, nodes_cnt)
        if k == left + 1:
            return root.val
        return self.get_kth(root.right, k - left - 1, nodes_cnt)


# 反向计数器、余数计数器, inorder, iteration
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        # write your code here
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

