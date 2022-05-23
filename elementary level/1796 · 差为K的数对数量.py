from typing import (
    List,
)

class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def k_difference(self, nums: List[int], target: int) -> int:
        # write your code here
        if len(nums) < 2:
            return 0

        s = set()
        cnt = 0
        for num in nums:
            if (num + target) in s:
                cnt += 1
            if (num - target) in s:
                cnt += 1
            s.add(num)

        return cnt



class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def k_difference(self, nums: List[int], target: int) -> int:
        # write your code here
        if len(nums) < 2:
            return 0

        s = set(nums)
        cnt = 0
        for num in nums:
            if (num + target) in s:
                cnt += 1
            if (num - target) in s:
                cnt += 1

        return cnt // 2



# 超时, T = O(n^2)
class Solution:
    """
    @param nums: a integer array
    @param target: 
    @return: return a integer
    """
    def k_difference(self, nums: List[int], target: int) -> int:
        # write your code here
        if len(nums) < 2:
            return 0

        cnt = 0
        for former in range(len(nums) - 1):
            for latter in range(former + 1, len(nums)):
                if abs(nums[former] - nums[latter]) == target:
                    cnt += 1

        return cnt
