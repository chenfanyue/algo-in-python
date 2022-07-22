from typing import (
    List,
)

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)

        return list(s1 & s2)


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        s2 = set(nums2)

        res = []
        for i in range(len(nums1)):
            if i > 0 and nums1[i] == nums1[i - 1]:
                continue
            if nums1[i] in s2:
                res.append(nums1[i])
        
        return res


# 归并的变形
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        nums1.sort()
        nums2.sort()

        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or nums1[i] != res[-1]: # 约束条件正着写
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res

