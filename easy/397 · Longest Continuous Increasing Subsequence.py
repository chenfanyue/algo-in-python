from typing import (
    List,
)

class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        if not a:
            return 0
        if len(a) == 1:
            return 1

        res = 1
        up = down = 1
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                up += 1
                res = max(res, down)
                down = 1
            elif a[i] == a[i - 1]:
                up += 1
                down += 1
            else:
                down += 1
                res = max(res, up)
                up = 1
            
        return max(res, up, down)


# 严格升降
class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a: List[int]) -> int:
        if not a:
            return 0
        if len(a) == 1:
            return 1

        res = 1
        up = down = 1
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                up += 1
                res = max(res, down)
                down = 1
            elif a[i] == a[i - 1]:
                res = max(res, up, down)
                up = down = 1
            else:
                down += 1
                res = max(res, up)
                up = 1
            
        return max(res, up, down)
