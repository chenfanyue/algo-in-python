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

# recommended, deal with current level
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        res = []
        if not root:
            return res
        
        path = []
        self.dfs(root, path, target, res)

        return res
    
    def dfs(self, root, path, target, res):
        path.append(root.val)
        if not root.left and not root.right:
            if sum(path) == target:
                res.append(list(path))
            path.pop()
            return

        if root.left:
            self.dfs(root.left, path, target, res)
        
        if root.right:
            self.dfs(root.right, path, target, res)
        
        path.pop()


class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        res = []
        if not root:
            return res
        
        path = []
        self.dfs(root, path, target, res)

        return res
    
    def dfs(self, root, path, target, res):
        path.append(root.val)
        if not root.left and not root.right:
            if sum(path) == target:
                res.append(list(path))
            path.pop()
            return

        for child in (root.left, root.right):
            if child:
                self.dfs(child, path, target, res)
        
        path.pop()


# recommended, 预处理机制，绝对单向图，站在已访问节点访问邻接点
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        res = []
        if not root:
            return res
        
        path = [root.val]
        self.dfs(root, path, target, res)

        return res
    
    def dfs(self, root, path, target, res):
        # check if arrived regression point
        if not root.left and not root.right:
            if sum(path) == target:
                res.append(list(path))
            return

        # visit next level
        # for child in (root.left, root.right):
        #     if child:
        #         path.append(child.val)
        #         self.dfs(child, path, target, res)
        #         path.pop()
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, path, target, res)
            path.pop()

        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, path, target, res)
            path.pop()


# not recommended, 不做合法性判断，无条件放行
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        res = []
        if not root:
            return res
        
        path = [root]
        self.dfs(root, path, target, res)

        return res
    
    def dfs(self, root, path, target, res):
        if not root:
            return
        if not root.left and not root.right:
            if sum(node.val for node in path) == target:
                res.append([node.val for node in path])

        path.append(root.left)
        self.dfs(root.left, path, target, res)
        path.pop()

        path.append(root.right)
        self.dfs(root.right, path, target, res)
        path.pop()

