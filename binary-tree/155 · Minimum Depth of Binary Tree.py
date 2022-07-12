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
from collections import deque

# bfs, deque
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


# bfs, arr
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0

        arr = [root]
        idx = 0
        level = 0

        while idx < len(arr):
            level += 1
            for _ in range(len(arr) - idx):
                node = arr[idx]
                idx += 1
                if not node.left and not node.right:
                    return level
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)


# divide and conquer
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return self.min_depth(root.left) + 1
        if root.right and not root.left:
            return self.min_depth(root.right) + 1
        
        left = self.min_depth(root.left)
        right = self.min_depth(root.right)
        return min(left, right) + 1

