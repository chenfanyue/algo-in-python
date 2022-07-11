from typing import (
    List,
)

# dfs
# each step select or not select
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
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


# dfs
# at next level append one more element to the dyn state from the remaining
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        sub = []
        subsets= []
        self.dfs(nums, 0, sub, subsets)

        return subsets

    def dfs(self, nums, remaining_first, sub, subsets):
        subsets.append(list(sub))
        
        for i in range(remaining_first, len(nums)):
            sub.append(nums[i])
            self.dfs(nums, i + 1, sub, subsets)
            sub.pop()


# dfs
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        sub = []
        res= [[]]
        self.dfs(nums, 0, sub, res)

        return res

    def dfs(self, nums, remaining_first, sub, res):
        # if remaining_first == len(nums):
        #     return
        
        for i in range(remaining_first, len(nums)):
            sub.append(nums[i])
            res.append(list(sub))
            self.dfs(nums, i + 1, sub, res)
            sub.pop()


# bfs
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        # nums.sort()
        res = [[]]
        idx = 0

        while idx < len(res):
            upper = res[idx]
            idx += 1
            for num in nums:
                if upper and num <= upper[-1]:
                    continue
                sub = list(upper)
                sub.append(num)
                res.append(sub)
        
        return res


# bfs
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        res = [[]]
        
        for num in nums:
            n = len(res)
            for i in range(n):
                sub = list(res[i])
                sub.append(num)
                res.append(sub)
        
        return res




# bfs, not recommended
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        nums.sort()
        res = [[]]
        last = [-1]
        idx = 0

        while idx < len(res):
            upper = res[idx]
            cur = last[idx] + 1
            idx += 1
            for i in range(cur, len(nums)):
                sub = list(upper)
                sub.append(nums[i])
                res.append(sub)
                last.append(i)
        
        return res
