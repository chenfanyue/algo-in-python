from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        left, right = 0, len(a) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
                return mid
            if a[mid] < a[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        left, right = 0, len(a) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
                return mid
            if a[mid] < a[mid - 1]:
                right = mid
            else:
                left = mid
        if a[left] > a[right]:
            return left
        return right


class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        left, right = 0, len(a) - 1
        while left < right:
            mid = left + (right - left) // 2
            if a[mid] > a[mid - 1] and a[mid] > a[mid + 1]:
                return mid
            if a[mid] < a[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        if left == right:
        	return left
        return -1


class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        for i in range(1, len(a) - 1):
            if a[i] > a[i - 1] and a[i] > a[i + 1]:
                return i