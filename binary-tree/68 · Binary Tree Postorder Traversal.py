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

# dfs
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)

        return res

    def dfs(self, root, res):
        if not root:
            return
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)


# divide and conquer
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left = self.postorder_traversal(root.left)
        right = self.postorder_traversal(root.right)
        return left + right + [root.val]


# 模拟递归调用栈，每个节点状态依次为0、1、2、3
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]: # v1
        # if not root:
        #     return []
        
        res = []
        stack = [(root, 0)]

        while stack:
            root, state = stack.pop()
            if not root:
                continue
            
            if state == 0:
                stack.append((root, 3))
                stack.append((root.right, 0))
                stack.append((root, 2))
                stack.append((root.left, 0))
                stack.append((root, 1))
            
            if state == 3:
                res.append(root.val)

        return res

    def postorder_traversal(self, root: TreeNode) -> List[int]: # v2
        res = []
        stack = [(root, 0)]

        while stack:
            root, state = stack.pop()
            if not root:
                continue
            
            if state == 0:
                stack.extend([
                    (root, 3),
                    (root.right, 0),
                    (root.left, 0)
                ])
            
            if state == 3:
                res.append(root.val)

        return res


# 前序、中序、后续统一模板，后续稍有不同
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack[-1]
            if not root.right or prev == root.right:
                res.append(stack.pop().val)
                prev = root
                root = None
            else:
                root = root.right
        
        return res


# Morris algo, 在镜像树上做前序遍历得到的序列跟在原树后续遍历的结果互为逆序
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        res = []

        while root:
            if root.right:
                probe = root.right
                while probe.left and probe.left != root:
                    probe = probe.left

                if not probe.left:
                    res.append(root.val)
                    probe.left = root
                    root = root.right
                else:
                    probe.left = None
                    root = root.left

            else:
                res.append(root.val)
                root = root.left
        
        res.reverse()
        
        return res

# ------------------------------
# 非递归，awful, not recommended
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        prev = None # 上一个访问的

        while stack:
            cur = stack[-1]
            if not prev or prev.left == cur or prev.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left == prev:
                if cur.right:
                    stack.append(cur.right)
            else:
                res.append(cur.val)
                stack.pop()
            prev = cur

        return res
