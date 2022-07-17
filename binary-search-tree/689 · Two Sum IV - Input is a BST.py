"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 中序遍历得到升序数组，相向双指针搜索该数组
class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        arr = self.get_arr(root)
        if len(arr) < 2:
            return None
        
        left, right = 0, len(arr) - 1
        while left < right:
            val = arr[left] + arr[right]
            if val == n:
                return [arr[left], arr[right]]
            if val < n:
                left += 1
            else:
                right -= 1
        
        return None

    def get_arr(self, root):
        arr = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            arr.append(root.val)

            if root.right:
                root = root.right
                continue

            root = None
        
        return arr


# 中序遍历的时候判断对应的数在不在哈希表里
class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        if not root:
            return None

        s = set()
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if (mate := n - root.val) in s:
                return [mate, root.val]
            s.add(root.val)

            if root.right:
                root = root.right
                continue

            root = None
        
        return None


# space complexity O(1)
class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    def twoSum(self, root, n):
        if not root:
            return None

        stack = []
        r = root

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            mate = n - root.val
            if self.contains(r, mate):
                return [root.val, mate]

            if root.right:
                root = root.right
                continue

            root = None
        
        return None

    def contains(self, root, val):
        if not root:
            return False

        if root.val == val:
            return True
        if root.val < val:
            return self.contains(root.right, val)
        else:
            return self.contains(root.left, val)

