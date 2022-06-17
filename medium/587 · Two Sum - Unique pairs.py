from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        nums_dict = dict()
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        res = 0
        for num in nums_dict:
            if (partner := target - num) in nums_dict and nums_dict[partner] != 0:
                if num != partner:
                    res += 1
                    nums_dict[num] = 0
                    nums_dict[partner] = 0
                else:
                    if nums_dict[num] >= 2:
                        res += 1
                        nums_dict[num] = 0
        
        return res


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        res_set = set()
        nums_set = set()
        for num in nums:
            if (partner := target - num) in nums_set:
                res_set.add((num, partner))
                if num != partner and (partner, num) in res_set:
                    res_set.remove((partner, num))
            nums_set.add(num)
        
        return len(res_set)


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        res_set = set()
        nums_set = set()
        for num in nums:
            if (partner := target - num) in nums_set:
                if (partner, num) not in res_set:
                    res_set.add((num, partner))
            nums_set.add(num)
        
        return len(res_set)


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        
        pairs = set()
        left, right = 0, len(nums) - 1
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                pairs.add((nums[left], nums[right]))
                left += 1
                right -= 1
            elif val < target:
                left += 1
            else:
                right -= 1
        
        return len(pairs)


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        
        left, right = 0, len(nums) - 1
        last_pair = (None, None)
        cnt = 0
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                if (nums[left], nums[right]) != last_pair:
                    cnt += 1
                    last_pair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif val < target:
                left += 1
            else:
                right -= 1
        
        return cnt


# too complicated conditions, not recommended
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        
        left, right = 0, len(nums) - 1
        cnt = 0
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                cnt += 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif val < target:
                left += 1
            else:
                right -= 1
        
        return cnt


# 将dict用作一个有状态数的集合，无状态数向有状态数的转变
# condition链的回溯
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        status_dict = dict()
        cnt = 0
        for num in nums:
            partner = target - num
            if partner in status_dict and status_dict[partner] == 1:
                cnt += 1
                status_dict[num] = 0
                status_dict[partner] = 0
            if partner not in status_dict:
                status_dict[num] = 1
        
        return cnt
