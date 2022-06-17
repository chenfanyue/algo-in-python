from typing import (
    List,
)

class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        # 1 <= x <= sum/k
        # l0/x + l1/x + .. + ln-1/x >= k
        if not l:
            return 0
        
        longest = sum(l) // k
        # if longest == 0:
        #     return 0

        left, right = 1, longest
        last_valid = 0
        # 用最短的路径将可能性遍历一遍
        while left <= right:
            mid = (left + right) // 2
            pieces = self.try_cut(l, mid)
            if pieces >= k:
                last_valid = mid
                left = mid + 1
            else:
                right = mid - 1

        return last_valid
    
    def try_cut(self, l, x):
        res = 0
        for wood in l:
            res += wood // x
        
        return res


class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        # 1 <= x <= sum/k
        # l0/x + l1/x + .. + ln-1/x >= k
        if not l:
            return 0
        
        longest = sum(l) // k
        if longest == 0:
            return 0

        left, right = 1, longest
        while left + 1 < right:
            mid = (left + right) // 2
            # print('left', left, 'right', right, 'mid', mid)
            pieces = self.try_cut(l, mid)
            # 将可能的范围缩小为两个
            if pieces > k:
                left = mid
            elif pieces == k:
                left = mid
            else:
                right = mid
        # print('right', right)
        # print('left', left)
        if self.try_cut(l, right) >= k:
            return right
        if self.try_cut(l, left) >= k:
            return left

        return 0
    
    def try_cut(self, l, x):
        res = 0
        for wood in l:
            res += wood // x
        
        return res
