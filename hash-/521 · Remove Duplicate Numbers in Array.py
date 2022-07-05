from typing import (
    List,
)

# in-place, unstable
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[res] = nums[i]
                res += 1
        
        return res


# extra space, stable
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = 0
        hashset = set()

        for num in nums:
            if num not in hashset:
                nums[res] = num
                res += 1
                hashset.add(num)
        
        return res
