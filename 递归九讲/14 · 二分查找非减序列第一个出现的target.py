from typing import (
    List,
)

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
        while find > 0 and nums[find - 1] == nums[find]:
            find -= 1
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

        left, right = 0, len(nums) - 1
        find = False
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                find = True
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if find == False:
            return -1
        while find > 0 and nums[mid - 1] == nums[mid]:
            mid -= 1
        return mid


算法效率差
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
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            return right
        return -1


算法效率差
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
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
