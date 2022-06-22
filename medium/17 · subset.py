from typing import (
    List,
)

# each step select or not select
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        nums.sort()
        path = []
        paths= []
        self.dfs(nums, 0, path, paths)

        return paths

    def dfs(self, nums, i, path, paths):
        if i == len(nums):
            paths.append(list(path))
            return
        
        path.append(nums[i])
        self.dfs(nums, i + 1, path, paths)

        path.pop()
        self.dfs(nums, i + 1, path, paths)


# at next level append one more element to the dyn state from the remaining
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        nums.sort()
        sub = []
        subsets= []
        self.dfs(nums, 0, [], subsets)

        return subsets

    def dfs(self, nums, remaining_first, sub, subsets):
        subsets.append(list(sub))
        
        for i in range(remaining_first, len(nums)):
            sub.append(nums[i])
            self.dfs(nums, i + 1, sub, subsets)
            sub.pop()



