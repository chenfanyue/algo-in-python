from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        find = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                find = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return find


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
