from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums: List[int]) -> int:
        if not nums:
            return float('-inf')
        # if len(nums) == 1:
        #     return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[0]:
                left = mid
            if nums[mid] < nums[-1]:
                right = mid
        
        return min(nums[left], nums[right])


class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
                
        return min(nums[start], nums[end])


