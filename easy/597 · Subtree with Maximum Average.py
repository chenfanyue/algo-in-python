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

# 跟随哈雷彗星的轨迹穿梭状态量组合
class Solution:
    """
    @param root: the root of binary tree
    @return: root of the subtree of maximum average
    """
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        max_average = -float('inf')
        max_tree = None
        res = self.dfs(root, max_tree, max_average)[0]
        
        return res
    
    def dfs(self, root, max_tree, max_average):
        if not root:
            return max_tree, max_average, 0, 0
        
        max_tree, max_average, left_sum, left_cnt = self.dfs(root.left, max_tree, max_average)
        max_tree, max_average, right_sum, right_cnt = self.dfs(root.right, max_tree, max_average)

        total_sum = left_sum + right_sum + root.val
        cnt = left_cnt + right_cnt + 1
        
        # update companion states
        total_average = total_sum / cnt
        if total_average > max_average:
            max_average = total_average
            max_tree = root
        
        return max_tree, max_average, total_sum, cnt


# 将一个或多个状态量封装到堆heap空间的一个结构体里
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        states = {
            'max_average': -float('inf'),
            'max_tree': None
        }
        
        self.dfs(root, states)
        
        return states['max_tree']
    
    def dfs(self, root, states):
        if not root:
            return 0, 0
        
        left_sum, left_cnt = self.dfs(root.left, states)
        right_sum, right_cnt = self.dfs(root.right, states)

        total_sum = left_sum + right_sum + root.val
        cnt = left_cnt + right_cnt + 1
        
        # update detached/transcendent states
        total_average = total_sum / cnt
        if total_average > states['max_average']:
            states['max_average'] = total_average
            states['max_tree'] = root
        
        return total_sum, cnt


# do NOT use this way, upgrade var from func-level to class-level
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def find_subtree2(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.max_average = -float('inf')
        self.max_tree = None
        
        self.dfs(root)
        
        return self.max_tree
    
    def dfs(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_cnt = self.dfs(root.left)
        right_sum, right_cnt = self.dfs(root.right)

        total_sum = left_sum + right_sum + root.val
        cnt = left_cnt + right_cnt + 1
        
        # update class-level attributes
        total_average = total_sum / cnt
        if total_average > self.max_average:
            self.max_average = total_average
            self.max_tree = root
        
        return total_sum, cnt


