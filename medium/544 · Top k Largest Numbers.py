from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        nums = sorted(nums, reverse=True)

        return nums[:k]


# offline algo
import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        
        res = []
        for _ in range(k):
            res.append(-heapq.heappop(h))
        
        return res


# online algo
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        
        res = [0] * k
        for i in range(k - 1, -1, -1):
            res[i] = heapq.heappop(h)
        
        return res


# partly quick sort
import random
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        self.quick_sort(nums, 0, len(nums) - 1, k)

        return nums[:k]
    
    def quick_sort(self, nums, start, end, k):
        if start >= k:
            return
        if start >= end:
            return
        
        left, right = start, end
        idx = random.randint(left, right)
        pivot = nums[idx]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.quick_sort(nums, start, right, k)
        self.quick_sort(nums, left, end, k)


# quick select
import random
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        self.quick_select(nums, 0, len(nums) - 1, k)

        res = nums[:k]
        res.sort(reverse=True)

        return res
    
    def quick_select(self, nums, start, end, k):
        if start == end:
            return
        
        left, right = start, end
        idx = random.randint(left, right)
        pivot = nums[idx]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if right - start + 1 >= k:
            self.quick_select(nums, start, right, k)
        if left - start + 1 <= k:
            self.quick_select(nums, left, end, k - (left - start))
        # return


class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        return heapq.nlargest(k, nums)

