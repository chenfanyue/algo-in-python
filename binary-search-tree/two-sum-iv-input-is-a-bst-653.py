# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s, q = set(), collections.deque([root])
        while q:
            root = q.popleft()
            if k - root.val in s:
                return True
            s.add(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        stack = [(root, 0)]
        while stack:
            root, state = stack.pop()
            if not root:
                continue
            
            if state == 0:
                stack.append((root.right, 0))
                stack.append((root, 3))
                stack.append((root.left, 0))
            
            if state == 3:
                if k - root.val in s:
                    return True
                s.add(root.val)
        
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        stack = [(root, 0)]
        while stack:
            root, state = stack.pop()
            if state == 0:
                if root.right:
                    stack.append((root.right, 0))
                stack.append((root, 3))
                if root.left:
                    stack.append((root.left, 0))
            
            if state == 3:
                if k - root.val in s:
                    return True
                s.add(root.val)
        
        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def dfs(root) -> bool:
            if not root:
                return False
            if k - root.val in s:
                return True
            s.add(root.val)
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
