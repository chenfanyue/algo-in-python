from typing import List

class Solution:
    
    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right, res = 0, len(nums) - 1, -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
