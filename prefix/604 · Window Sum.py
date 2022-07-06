from typing import (
    List,
)

# 滚动推导，滑动窗口
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        n = len(nums)
        if k >= n:
            return [sum(nums)]
        
        res = [0] * (n + 1 - k)
        for i in range(k):
            res[0] += nums[i]
        
        for i in range(1, n + 1 - k):
            r = i + k -1
            res[i] = res[i - 1] - nums[i - 1] + nums[r]
        
        return res


# prefix sum
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        n = len(nums)
        if k >= n:
            return [sum(nums)]
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        res = []

        for i in range(n + 1 - k):
            r = i + k -1
            res.append(prefix_sum[r + 1] - prefix_sum[i])
        
        return res


# a bit faster
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        n = len(nums)
        if k >= n:
            return [sum(nums)]
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        res = [0] * (n + 1 - k)

        for i in range(n + 1 - k):
            r = i + k -1
            res[i] = prefix_sum[r + 1] - prefix_sum[i]
        
        return res


# 极其巧妙的滑动窗口
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        n = len(nums)
        if k >= n:
            return [sum(nums)]
        
        val = 0
        for i in range(k - 1):
            val += nums[i]
        
        res = [0] * (n + 1 - k)

        for i in range(n + 1 - k):
            r = i + k -1
            val += nums[r]
            res[i] = val
            val -= nums[i]
        
        return res

