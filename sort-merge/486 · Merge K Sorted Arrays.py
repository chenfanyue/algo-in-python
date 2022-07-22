from typing import (
    List,
)

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        res = []
        for a in arrays:
            res += a
        
        res.sort()

        return res


# heapq
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        res = []
        heap = []

        for i, arr in enumerate(arrays):
            if not arr:
                continue
            heapq.heappush(heap, (arr[0], i, 1))

        while heap:
            v, i, j = heap[0]
            res.append(v)
            if j < len(arrays[i]):
                heapq.heapreplace(heap, (arrays[i][j], i, j + 1))
            else:
                heapq.heappop(heap)
        
        return res


import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        res = []
        heap = []

        for i, arr in enumerate(arrays):
            if not arr:
                continue
            heapq.heappush(heap, (arr[0], i, 1))

        while heap:
            v, i, j = heapq.heappop(heap)
            res.append(v)
            if j < len(arrays[i]):
                heapq.heappush(heap, (arrays[i][j], i, j + 1))
        
        return res



# not recommended
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        res = []
        h, k = [], len(arrays)

        cols = [0] * k
        for i in range(k):
            if not arrays[i]:
                continue
            heapq.heappush(h, (arrays[i][0], i))
            cols[i] += 1

        while h:
            v, i = heapq.heappop(h)
            res.append(v)
            if (j := cols[i]) < len(arrays[i]):
                heapq.heappush(h, (arrays[i][j], i))
                cols[i] += 1

        return res
