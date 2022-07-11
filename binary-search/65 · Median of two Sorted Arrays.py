from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def find_median_sorted_arrays(self, a: List[int], b: List[int]) -> float:
        if not a and not b:
            return .0
        if a and not b:
            return self.find_median(a)
        if b and not a:
            return self.find_median(b)

        res, a_start, b_start = self.find_kth_smallest(a, b)
        
        n, m = len(a), len(b)
        a_val = float('inf') if a_start >= n else a[a_start]
        b_val = float('inf') if b_start >= m else b[b_start]
        if (n + m) & 1 == 0:
            res += min(a_val, b_val)
            res = res / 2
        
        return res + .0
    
    def find_median(self, arr):
        n = len(arr)
        mid = (n - 1) >> 1
        if n & 1:
            return arr[mid] + .0
        return (arr[mid] + arr[mid + 1]) / 2

    def find_kth_smallest(self, a: List[int], b: List[int]):
        n, m = len(a), len(b)
        # offset = 1 if (n + m) & 1 else 0
        # k = (n + m) >> 1 + offset
        k = (n + m + 1) >> 1
        a_start = b_start = 0

        while k > 1:
            a_end = a_start + k // 2 - 1
            b_end = b_start + k // 2 - 1
            a_val = float('inf') if a_end >= n else a[a_end]
            b_val = float('inf') if b_end >= m else b[b_end]
            if a_val < b_val:
                a_start = a_end + 1
            else:
                b_start = b_end + 1
            k -= k // 2
        
        a_val = float('inf') if a_start >= n else a[a_start]
        b_val = float('inf') if b_start >= m else b[b_start]

        if a_val < b_val:
            return a_val, a_start + 1, b_start
        return b_val, a_start, b_start + 1


