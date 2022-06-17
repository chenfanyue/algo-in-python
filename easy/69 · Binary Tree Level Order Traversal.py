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

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        q = collections.deque()
        # q = collections.deque([root])
        q.append(root)
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        return res


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        q = collections.deque()
        # q = collections.deque([root])
        q.append(root)
        res = []

        while q:
            res.append([e.val for e in q])
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res


# new old array
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        current_level = [root]
        res = []

        while current_level:
            buf = []
            next_level = []
            for node in current_level:
                buf.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(buf)
            current_level = next_level
        
        return res


# recommended
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        current_level = [root]
        next_level = []
        res = []

        while current_level:
            buf = []
            for node in current_level:
                buf.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level.clear()
            res.append(buf)
            current_level, next_level = next_level, current_level
        
        return res


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        current_q = collections.deque([root])
        next_q = collections.deque()
        res = []

        while current_q:
            buf = []
            while current_q:
                node = current_q.popleft()
                buf.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.append(buf)
            current_q, next_q = next_q, current_q
        
        return res


# zigzag print, follow up
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        q = collections.deque()
        # q = collections.deque([root])
        q.append(root)
        res = []

        to_left = False
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if to_left:
                level.reverse()
            res.append(level)
            to_left = not to_left
        
        return res


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        
        q = collections.deque([root, None])
        res = []
        buf = []

        while q:
            node = q.popleft()
            if node is None:
                res.append(buf)
                if not q:
                    return res
                q.append(None)
                buf = []
                continue
            buf.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
