from typing import (
    List,
)

class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def search_subarray(self, arr: List[int], k: int) -> int:
        if not arr:
            return -1

        pre, pre_idx = 0, {0: -1}
        
        for i in range(len(arr)):
            pre += arr[i]
            if pre - k in pre_idx:
                return i - pre_idx[pre - k]
            if pre not in pre_idx:
                pre_idx[pre] = i
        
        return -1


class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def search_subarray(self, arr: List[int], k: int) -> int:
        if not arr:
            return -1

        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        pre_idx = {}
        for i in range(len(prefix)):
            if prefix[i] - k in pre_idx:
                return i - pre_idx[prefix[i] - k]
            if prefix[i] not in pre_idx:
                pre_idx[prefix[i]] = i
        
        return -1



# Time Limit Exceeded
class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """
    def search_subarray(self, arr: List[int], k: int) -> int:
        if not arr:
            return -1

        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        for i in range(n):
            for j in range(i + 1):
                if prefix[i + 1] - prefix[j] == k:
                    return i - j + 1
        
        return -1



