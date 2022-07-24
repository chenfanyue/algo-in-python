from typing import (
    List,
)

# 优雅高效写法
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1, -1]
        
        target = abs(target)
        j = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[j] < target:
                continue
            if nums[i] - nums[j] == target:
                return [nums[j], nums[i]]

            while nums[i] - nums[j] > target:
                j += 1
                if j == i:
                    break
                if nums[i] - nums[j] == target:
                    return [nums[j], nums[i]]
        
        return [-1, -1]


# 2pointers, same direction
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums or n < 2:
            return [-1, -1]
        
        target = abs(target)
        j = 1

        for i in range(n):
            j = max(j, i + 1)
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j == n:
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        
        return [-1, -1]


# 2pointers, same direction + binary search
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums or n < 2:
            return [-1, -1]
        
        target = abs(target)
        j = 1

        for i in range(n):
            j = max(j, i + 1)
            j = self.binary_search(nums, j, nums[i] + target)
            if j == -1:
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]
        
        return [-1, -1]

    def binary_search(self, nums, j, target):
        left, right = j, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return -1


# using hashset
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return [-1, -1]
        
        target = abs(target)
        hashset = set()

        for num in nums:
            if num - target in hashset:
                return [num - target, num]
            hashset.add(num)
        
        return [-1, -1]
