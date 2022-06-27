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

# bfs, queue and counter window
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        q = collections.deque([root])
        into = 0

        while q:
            into += 1
            if into == level:
                return sum(node.val for node in q)
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return 0 # level unbound


# bfs, list and floating counter window of dynamic size
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        q = [root]
        level_first = level_last = 0
        into = 0

        while True:
            into += 1
            if into == level:
                return sum(q[i].val for i in range(level_first, level_last + 1))
            
            add = 0
            for i in range(level_first, level_last + 1):
                node = q[i]
                if node.left:
                    q.append(node.left)
                    add += 1
                if node.right:
                    q.append(node.right)
                    add += 1
            
            if add == 0:
                break
            
            level_first = level_last + 1
            level_last = level_first + add - 1
        
        return 0


# dfs, with detached state
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        res = {'total': 0}
        into = 1

        self.dfs(root, into, level, res)
        
        return res['total']

    def dfs(self, root, into, level, res):
        if not root:
            return
        if into == level:
            res['total'] += root.val
            return
        
        self.dfs(root.left, into + 1, level, res)
        self.dfs(root.right, into + 1, level, res)


# not recommended, extra cost, 携带状态量递进，回溯阶段更新状态量并返回给上一层
# dfs, with carrying state
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        res = 0
        into = 1

        return self.dfs(root, into, level, res)

    def dfs(self, root, into, level, res):
        if not root:
            return res
        if into == level:
            res += root.val
            return res
        
        res = self.dfs(root.left, into + 1, level, res)
        res = self.dfs(root.right, into + 1, level, res)

        return res


# divide and conquer, recommended, 无外界参照系，抓住level进行逻辑推断
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        if 1 == level:
            return root.val
        
        left = self.level_sum(root.left, level - 1)
        right = self.level_sum(root.right, level - 1)

        return left + right


# divide and conquer, recommended, 利用vertical刻度线作参照系
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        if not root:
            return 0
        
        start_level = 1

        return self.dac(root, start_level, level)

    def dac(self, root, start_level, level):
        if not root:
            return 0
        
        if start_level == level:
            return root.val
        
        left = self.dac(root.left, start_level + 1, level)
        right = self.dac(root.right, start_level + 1, level)

        return left + right

