from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        if not a or target < a[0] or target > a[-1]:
            return [-1, -1]

        first = self.find_first(a, 0, len(a) - 1, target)
        if first == -1:
            return [-1, -1]

        last = self.find_last(a, first, len(a) - 1, target)

        return [first, last]

    def find_first(self, a, left, right, target):
        res = -1
        while left <= right:
            mid = (left + right) >> 1
            if target == a[mid]:
                res = mid
                right = mid - 1
            elif target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return res

    def find_last(self, a, left, right, target):
        res = -1
        while left <= right:
            mid = (left + right) >> 1
            if target == a[mid]:
                res = mid
                left = mid + 1
            elif target < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return res
