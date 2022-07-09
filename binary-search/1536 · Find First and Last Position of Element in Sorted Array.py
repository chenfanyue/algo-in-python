from typing import (
    List,
)

# 重点，二分法的正确用法
class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def search_range(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1

        start = self.get_first(nums, left, right, target)
        if start == -1:
            return [-1, -1]
        
        end = self.get_last(nums, start, right, target)

        return [start, end]
    
    def get_first(self, nums, left, right, target):
        while left + 1 < right:
            mid = (left + right) >> 1
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
        
    def get_last(self, nums, left, right, target):
        while left + 1 < right:
            mid = (left + right) >> 1
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
