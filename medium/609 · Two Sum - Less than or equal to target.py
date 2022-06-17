from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        cnt = 0
        n = len(nums)
        for left in range(n - 1):
            right = n - 1
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            cnt += right - left

        return cnt


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        cnt = 0
        n = len(nums)
        right = n - 1
        for left in range(n - 1):
            while left < right and nums[left] + nums[right] > target:
                right -= 1
            if left >= right:
                break
            cnt += right - left

        return cnt


class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        cnt = 0
        left, right = 0, len(nums) - 1
        while left < right:
            val = nums[left] + nums[right]
            if val > target:
                right -= 1
            else:
                cnt += right - left
                left += 1

        return cnt
