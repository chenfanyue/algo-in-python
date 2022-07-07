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

# dfs
class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leaf_sum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = {'res': 0}
        self.dfs(root, res)

        return res['res']
    
    def dfs(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res['res'] += root.val
            return
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)


# divide and conquer
class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leaf_sum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        return left + right


# bfs
class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leaf_sum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        from collections import deque
        q = deque([root])

        while q:
            cur = q.popleft()

            if not cur.left and not cur.right:
                res += cur.val
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return res


# inorder traverse, iteration
class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leaf_sum(self, root: TreeNode) -> int:
        res = 0
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if not root.left and not root.right:
                res += root.val
            
            if root.right:
                root = root.right
                continue
            
            root = None

        return res


