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

# 抽象变量定义，一个变量赋予两种含义
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        return self.abstract_height(root) != -1
        
    def abstract_height(self, root):
        if not root:
            return 0
        
        left = self.abstract_height(root.left)
        right = self.abstract_height(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1


# 跟随状态，跟着主逻辑走，顺便求出第二结果
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[0]
        
    def dfs(self, root):
        if not root:
            return True, 0
        
        left_tag, left_height = self.dfs(root.left)
        if not left_tag:
            return False, 0
        
        right_tag, right_height = self.dfs(root.right)
        if not right_tag:
            return False, 0

        tag = abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1

        return tag, height


# 局部函数，嵌套递归，记忆化搜索 // 稳妥写法
class Solution:
    """
    @param root: root of a binary tree.
    @return: whether the binary tree is balanced.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        def height(root, memo):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]

            left = height(root.left, memo)
            right = height(root.right, memo)

            res = max(left, right) + 1
            
            memo[root] = res
            return res

        def worker(root, memo):
            if not root:
                return True
            
            return worker(root.left, memo) and \
                worker(root.right, memo) and \
                abs(height(root.left, memo) - height(root.right, memo)) <= 1
        
        memo = {}

        return worker(root, memo)


# 局部函数，嵌套递归，记忆化搜索 // 高级写法
class Solution:
    """
    @param root: root of a binary tree.
    @return: whether the binary tree is balanced.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        def height(root, memo):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]

            left = height(root.left, memo)
            right = height(root.right, memo)

            res = max(left, right) + 1
            
            memo[root] = res
            return res

        def worker(root):
            if not root:
                return True
            
            return worker(root.left) and \
                worker(root.right) and \
                abs(height(root.left, memo) - height(root.right, memo)) <= 1
        
        memo = {}

        return worker(root)



# ----------------------------
# a bit slower, 要到外层空间搜索变量
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def is_balanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]

            left = height(root.left)
            right = height(root.right)

            res = max(left, right) + 1
            
            memo[root] = res
            return res

        def worker(root):
            if not root:
                return True
            
            return worker(root.left) and \
                worker(root.right) and \
                abs(height(root.left) - height(root.right)) <= 1
        
        memo = {}

        return worker(root)


