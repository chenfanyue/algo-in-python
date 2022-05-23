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
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


遇到大规模重复数据，时间超限
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1
        find = self.binary_search_helper(nums, target)
        if find == -1:
            return -1
        last = len(nums) - 1
        while find < last and nums[find + 1] == nums[find]:
            find += 1
        return find

    def binary_search_helper(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


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
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1


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
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return find

