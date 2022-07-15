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

# 纯逻辑分治
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []
        
        if root.val > k2:
            return self.search_range(root.left, k1, k2)
        
        if root.val < k1:
            return self.search_range(root.right, k1, k2)
        
        left = self.search_range(root.left, k1, k2)
        right = self.search_range(root.right, k1, k2)
        return left + [root.val] + right


# inorder dfs, directly return value, very important
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []
        
        res = []
        left = self.search_range(root.left, k1, k2)
        res.extend(left)
        
        if k1 <= root.val <= k2:
            res.append(root.val)
        
        right = self.search_range(root.right, k1, k2)
        res.extend(right)

        return res


# inorder dfs
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        res = []
        self.dfs(root, k1, k2, res)

        return res
    
    def dfs(self, root, k1, k2, res):
        if not root:
            return
        
        self.dfs(root.left, k1, k2, res)

        if k1 <= root.val <= k2:
            res.append(root.val)
        
        self.dfs(root.right, k1, k2, res)


# inorder dfs + divide and conquer, 运用抽象返回值
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []
        
        left = self.search_range(root.left, k1, k2)
        right = self.search_range(root.right, k1, k2)

        if k1 <= root.val <= k2:
            return left + [root.val] + right
        return left + right


# 模拟递归调用栈
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        res = []
        stack = [(root, 0)]

        while stack:
            root, state = stack.pop()
            if not root:
                continue

            if state == 0:
                stack.extend([
                    (root.right, 0),
                    (root, 3),
                    (root.left, 0)
                ])

            if state == 3:
                if k1 <= root.val <= k2:
                    res.append(root.val)
            # if state == 3 and k1 <= root.val <= k2:
            #     res.append(root.val)

        return res


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        res = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if k1 <= root.val <= k2:
                res.append(root.val)
            
            if root.right:
                root = root.right
                continue

            root = None

        return res



