# the first chance to find a target
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            # cut = (end - start) // 2
            # mid = start + cut
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        # for i in range(start, end + 1):
        #     if nums[i] == target:
        #         return i
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


# to find the most left target
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            # cut = (end - start) // 2
            # mid = start + cut
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            else:
                start = mid
        # for i in range(start, end + 1):
        #     if nums[i] == target:
        #         return i
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


# to find the most right target
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            # cut = (end - start) // 2
            # mid = start + cut
            mid = start + (end - start) // 2
            if target >= nums[mid]:
                start = mid
            else:
                end = mid
        # for i in range(start, end + 1):
        #     if nums[i] == target:
        #         return i
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        # triple search
        start = 0
        end = len(nums) - 1
        while start + 2 < end:
            cut = (end - start) // 3
            mid1 = start + cut
            mid2 = mid1 + cut
            num1 = nums[mid1]
            num2 = nums[mid2]
            if num1 == target:
                return mid1
            elif num2 == target:
                return mid2
            elif num1 > target:
                end = mid1 - 1
            elif num1 < target < num2:
                start = mid1 + 1
                end = mid2 - 1
            else:
                start = mid2 + 1
        for i in range(start, end + 1):
            if nums[i] == target:
                return i
        return -1
