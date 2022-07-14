from typing import (
    List,
)

class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        path = []
        res = []
        self.dfs(nums, 0, path, res)

        return res[0]
    
    def dfs(self, nums, start, path, res):
        if start == len(nums):
            self.update_res(path, res)
        
        added = False
        for i in range(start, len(nums)):
            if path and nums[i] % path[-1] != 0:
                continue
            path.append(nums[i])
            added = True
            self.dfs(nums, i + 1, path, res)
            path.pop()
        
        if not added:
            self.update_res(path, res)
    
    def update_res(self, path, res):
        if not res:
            res.append(list(path))
            return
        if len(path) <= len(res[0]):
            return
        else:
            res.clear()
            res.append(list(path))
            return


class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n

        dp_max = (-1, 0) # index, value
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = dp[j] + 1 if dp[j] + 1 > dp[i] else dp[i]
            dp_max = (i, dp[i]) if dp[i] > dp_max[1] else dp_max
        
        res = []
        big = dp_max[1]
        for i in range(dp_max[0], -1, -1):
            if big % nums[i] == 0:
                res.append(nums[i])
                big = nums[i]
        
        res.reverse()
        
        return res
        
