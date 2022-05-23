from typing import (
    List,
)

class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        max_value = float('-inf')
        for num in nums:
            if num > max_value:
                max_value = num
        return max_value


class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        max_value = float('-inf')
        for num in nums:
            max_value = max(max_value, num)
        return max_value


class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        if len(nums) == 1:
            return nums[0]
        tail = nums.pop()
        todo_max = self.max_num(nums)
        if todo_max > tail:
            return todo_max
        return tail


class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        max_value = float('-inf')
        return self.max_num_helper(nums, max_value)
    
    def max_num_helper(self, nums, max_value):
        if len(nums) == 0:
            return max_value
        tail = nums.pop()
        if tail > max_value:
            max_value = tail
        return self.max_num_helper(nums, max_value)
