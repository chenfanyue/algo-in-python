class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return -1


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        if target < nums[0] or target > nums[-1]:
            return -1
        return self.findPosition_helper(nums, 0, len(nums) - 1, target)

    def findPosition_helper(self, nums, start, end, target):
        if start > end:
            return -1
        middle = start + (end - start) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = middle - 1
            return self.findPosition_helper(nums, start, end, target)
        else:
            start = middle + 1
            return self.findPosition_helper(nums, start, end, target)


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums: List[int], target: int, start: int = 0) -> int:
        # write your code here
        if start == len(nums):
            return -1
        if nums[start] == target:
            return start
        return self.findPosition(nums, target, start + 1)


三分查找
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1
        while start + 3 <= end:
            cut = (end - start) // 3
            mid1 = start + cut
            mid2 = mid1 + cut
            if nums[mid1] == target:
                return mid1
            elif nums[mid2] == target:
                return mid2
            elif nums[mid1] > target:
                end = mid1 - 1
            elif nums[mid1] < target < nums[mid2]:
                start = mid1 + 1
                end = mid2 - 1
            else:
                start = mid2 + 1
        for i in range(start, end + 1):
            if nums[i] == target:
                return i
        return -1
