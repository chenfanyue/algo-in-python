from typing import (
    List,
)


# counting sort, recommended
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) < 3:
            return
        
        cnt = [0] * 3
        for val in nums:
            if 0 == val:
                cnt[0] += 1
            elif 1 == val:
                cnt[1] += 1
            else:
                cnt[2] += 1
        
        i = -1
        color = -1
        for color_times in cnt:
            color += 1
            for _ in range(color_times):
                i += 1
                nums[i] = color


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) < 3:
            return
        
        # cnt = {0: 0, 1: 0, 2: 0}
        cnt = {i : 0 for i in range(3)}
        for color in nums:
            cnt[color] += 1
        
        i = -1
        for color in cnt:
            for _ in range(cnt[color]):
                i += 1
                nums[i] = color


# counting sort, recommended
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) < 3:
            return
        
        cnt = [0] * 3
        for val in nums:
            if 0 == val:
                cnt[0] += 1
            elif 1 == val:
                cnt[1] += 1
            else:
                cnt[2] += 1
        
        i = -1
        for color, times in enumerate(cnt):
            for _ in range(times):
                i += 1
                nums[i] = color


# still a bit puzzled
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and nums[left] <= 1:
                left += 1
            while left < right and nums[right] > 1:
                right -= 1
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = 0
        while left < right:
            while left < right and nums[left] < 1:
                left += 1
            while left < right and nums[right] > 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) < 3:
            return
        
        left, p, right = 0, 0, len(nums) - 1
        while p <= right:
            if nums[p] == 0:
                nums[left], nums[p] = nums[p], nums[left]
                left += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p], nums[right] = nums[right], nums[p]
                right -= 1


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None or len(nums) < 3:
            return
        
        n = len(nums)
        i = 0
        color = -1
        for _ in range(2):
            color += 1
            for j in range(i, n):
                if nums[j] == color:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if nums is None:
            return
        low = 0
        mid = 0
        for i in range(len(nums)):
            val = nums[i]
            nums[i] = 2
            if val < 2:
                nums[mid] = 1
                mid += 1
            if val < 1:
                nums[low] = 0
                low += 1
