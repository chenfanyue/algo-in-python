from typing import (
    List,
)

# 按字典序升序的数组排列的下一个状态
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def next_permutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i > 0:
            j = n - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j], nums[i-1] = nums[i-1], nums[j]
        
        self.swap_list(nums, i, n - 1)

        return nums
    
    def swap_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
