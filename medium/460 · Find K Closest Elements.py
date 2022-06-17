from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        if not a or k == 0:
            return []
        
        if target <= a[0]:
            return a[:k]
        if target >= a[-1]:
            return a[-1:-k-1:-1]
        larger_index = self.find_first_larger_index(a, target)

        left, right = larger_index - 1, larger_index
        
        return self.get_k_nums(a, left, right, target, k)
    
    def find_first_larger_index(self, a, target):
        left, right = 0, len(a) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if a[mid] >= target:
                right = mid
            else:
                left = mid
        if a[left] >= target:
            return left
        if a[right] >= target:
            return right
    
    def get_k_nums(self, a, left, right, target, k):
        res = []
        while left >= 0 and right < len(a) and k > 0:
            if abs(a[left] - target) <= abs(a[right] - target):
                res.append(a[left])
                left -= 1
            else:
                res.append(a[right])
                right += 1
            k -= 1
        
        if k == 0:
            return res
        
        if left < 0:
            for _ in range(k):
                res.append(a[right])
                right += 1
            return res
        
        for _ in range(k):
            res.append(a[left])
            left -= 1
        return res
