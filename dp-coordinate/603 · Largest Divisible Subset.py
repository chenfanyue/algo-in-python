from typing import (
    List,
)

# dp-coordinate, 值键映射，回溯链，伴生数据结构，分别从a/b集合进入交集的性能区别 
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        val2idx = {nums[i]: i for i in range(len(nums))}

        n = len(nums)
        dp = [1] * n
        came = [-1] * n

        dp_max = (-1, 0) # index, value
        for i in range(1, n):
            factors = self.get_factors(nums[i])
            for f in factors:
                if f not in val2idx:
                    continue
                if (s := dp[val2idx[f]] + 1) > dp[i]:
                    dp[i] = s
                    came[i] = val2idx[f]
            dp_max = (i, dp[i]) if dp[i] > dp_max[1] else dp_max
        
        res, i = [], dp_max[0]
        while i != -1:
            res.append(nums[i])
            i = came[i]
        
        res.reverse()
        
        return res
        
    def get_factors(self, num):
        res = set([1])
        if num == 1:
            return res
        
        for i in range(2, int(math.sqrt(num)) + 1):
            # if i in res:
            #     break
            if num % i == 0:
                res.update([i, num // i])
        
        return res


# over time
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


# over time
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
