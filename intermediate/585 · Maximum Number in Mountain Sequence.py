from typing import (
    List,
)

# 这道题设计的有问题
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return float('-inf')
        if len(nums) == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[-1] > nums[-2]:
            return nums[-1]
        
        left, right = 1, len(nums) - 2
        while left <= right:
            x = (left + right) // 2
            if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
                return nums[x]
            if nums[x] < nums[x - 1]:
                right = x - 1
                continue
            left = x + 1


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        if not nums:
            return float('-inf')
        if len(nums) == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[-1] > nums[-2]:
            return nums[-1]
        
        left, right = 1, len(nums) - 2
        while left + 1 < right:
            x = (left + right) // 2
            if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
                return nums[x]
            if nums[x] < nums[x - 1]:
                right = x
                continue
            left = x
        return max(nums[left], nums[right])



