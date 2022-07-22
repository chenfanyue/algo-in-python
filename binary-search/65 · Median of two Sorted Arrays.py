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


class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

