class Solution:
    """
    @param arr: an array of non-negative integers
    @return: minimum number of elements
    """
    def min_elements(self, arr: List[int]) -> int:
        if not arr:
            return 0
        
        pivot = sum(arr) >> 1
        arr.sort(reverse=True)
        cnt = 0
        total = 0

        for v in arr:
            total += v
            cnt += 1
            if total > pivot:
                return cnt
