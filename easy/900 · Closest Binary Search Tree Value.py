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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        less, larger = -float('inf'), float('inf')

        while root:
            if root.val == target:
                return root.val
            elif root.val < target:
                less = root.val
                root = root.right
            else:
                larger = root.val
                root = root.left
        
        if target - less < larger - target:
            return int(less)
        return int(larger)


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        less, larger = -float('inf'), float('inf')

        return self.helper(root, target, less, larger)

    def helper(self, root, target, less, larger):
        if not root:
            return int(less) if target - less < larger - target else int(larger)
        
        if root.val == target:
            return root.val
        elif root.val < target:
            less = root.val
            return self.helper(root.right, target, less, larger)
        else:
            larger = root.val
            return self.helper(root.left, target, less, larger)


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        lower, upper = root, root

        lower, upper = self.helper(root, target, lower, upper)

        return lower.val if abs(lower.val - target) < abs(upper.val - target) else upper.val

    def helper(self, root, target, lower, upper):
        if not root:
            return lower, upper
        
        if root.val == target:
            return root, root
        elif root.val < target:
            lower = root
            return self.helper(root.right, target, lower, upper)
        else:
            upper = root
            return self.helper(root.left, target, lower, upper)
        

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        # lower, the last node which is less than target
        # upper, the last node which is larger than target
        lower, upper = root, root

        while root:
            if root.val == target:
                return root.val
            elif root.val < target:
                lower = root
                root = root.right
            else:
                upper = root
                root = root.left

        return lower.val if abs(lower.val - target) < abs(upper.val - target) else upper.val


# binary tree inorder traversal
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        stack, last_less = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val >= target:
                if abs(last_less - target) < abs(root.val - target):
                    return last_less
                return root.val
            
            last_less = root.val
            root = root.right
        
        return last_less


# use a register to update the closest node-value
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        closest = root.val

        while root:
            if root.val == target:
                return root.val
            closest = min(root.val, closest, key=lambda x: abs(x - target))
            root = root.left if target < root.val else root.right

        return closest


# convert to ascending array
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # write your code here
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key=lambda x: abs(target - x))



