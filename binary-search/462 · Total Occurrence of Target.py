from typing import (
    List,
)

class Solution:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def total_occurrence(self, a: List[int], target: int) -> int:
        if not a or target < a[0] or target > a[-1]:
            return 0

        first = self.get_first_idx(a, target)
        if first == -1:
            return 0
        last = self.get_last_idx(a, target)

        return last - first + 1

    def get_first_idx(self, a, target):
        left, right = 0, len(a) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) >> 1
            if target == a[mid]:
                last = mid
                right = mid - 1
            elif target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return last

    def get_last_idx(self, a, target): # v1
        left, right = 0, len(a) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) >> 1
            if target == a[mid]:
                last = mid
                left = mid + 1
            elif target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return last

    def get_last_idx(self, a, target): # v2
        left, right = 0, len(a) - 1
        
        while left + 1 < right:
            mid = (left + right) >> 1
            if target >= a[mid]:
                left = mid
            else:
                right = mid
        if a[right] == target:
            return right
        if a[left] == target:
            return left
        return -1
