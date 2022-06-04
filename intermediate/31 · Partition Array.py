from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # if left == n:
        #     return n
        # if left - right == 2:
        #     return left - 1
        return left
