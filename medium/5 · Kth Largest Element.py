from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        if not nums or not (1 <= k <= len(nums)):
            return -1
        
        nums.sort()

        return nums[-k]
        # nums.sort(reverse=True)
        # return nums[k - 1]


# quick sort
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        if not nums or not (1 <= k <= len(nums)):
            return -1

        self.quick_sort(nums, 0, len(nums) - 1)

        return nums[-k]

    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)
        return


# quick select, k-th largest
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        if not nums or not (1 <= k <= len(nums)):
            return -1

        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        mid = (start + end) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right - start + 1:
            return self.quick_select(nums, start, right, k)
        elif k >= left - start + 1:
            return self.quick_select(nums, left, end, k - (left - start))
        else:
            return pivot


# quick select, k-th largest turns into
# find index=(n-k) number after ascending sort
class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        if not nums or not (1 <= k <= len(nums)):
            return None

        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    def quick_select(self, nums, start, end, i):
        if start == end:
            return nums[start]

        mid = (start + end) // 2
        pivot = nums[mid]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if i <= right:
            return self.quick_select(nums, start, right, i)
        elif i >= left:
            return self.quick_select(nums, left, end, i)
        else:
            return pivot



