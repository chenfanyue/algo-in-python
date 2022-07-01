from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarray_sum(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        stats = {}
        for i in range(len(prefix_sum)):
            if prefix_sum[i] in stats:
                return [stats[prefix_sum[i]], i - 1]
            stats[prefix_sum[i]] = i


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarray_sum(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        stats = {}
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in stats:
                stats[prefix_sum[i]] = []
            stats[prefix_sum[i]].append(i)
        
        for arr in stats.values():
            if len(arr) >= 2:
                return [arr[0], arr[1] - 1]
        

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarray_sum(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        stats = {0: 0}
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            if prefix_sum[i + 1] in stats:
                return [stats[prefix_sum[i + 1]], i]
            stats[prefix_sum[i + 1]] = i + 1


# follow up, 求出全部和为0的子数组
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarray_sum(self, nums: List[int]) -> List[int]:
        # write your code here
        if not nums:
            return []
        
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        stats = {}
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in stats:
                stats[prefix_sum[i]] = []
            stats[prefix_sum[i]].append(i)
        
        res = []
        for arr in stats.values():
            if len(arr) == 2:
                res.append([arr[0], arr[1] - 1])
            if len(arr) > 2:
                for i in range(len(arr) - 1):
                    for j in range(1, len(arr)):
                        res.append([arr[i], arr[j] - 1])
        
        return res
