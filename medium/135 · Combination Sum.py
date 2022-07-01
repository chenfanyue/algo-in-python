from typing import (
    List,
)

# 逼近法/消除法, dfs
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        if not candidates:
            return []
        
        arr = sorted(set(candidates))

        start = 0
        comb = []
        res = []
        gap = target
        self.dfs(arr, start, comb, gap, res)

        return res
    
    def dfs(self, arr, start, comb, gap, res):
        if gap == 0:
            res.append(list(comb))
            return
        
        for i in range(start, len(arr)):
            if arr[i] > gap:
                return
            comb.append(arr[i])
            self.dfs(arr, i, comb, gap - arr[i], res)
            comb.pop()


# 累加法/超级剪枝, dfs
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        if not candidates:
            return []
        
        arr = sorted(set(candidates))

        start = 0
        comb = []
        res = []
        self.dfs(arr, start, comb, 0, target, res)

        return res
    
    def dfs(self, arr, start, comb, comb_sum, target, res):
        if comb_sum == target:
            res.append(list(comb))
            return
        
        for i in range(start, len(arr)):
            comb.append(arr[i])
            comb_sum += arr[i]
            if comb_sum > target:
                comb.pop()
                return
            self.dfs(arr, i, comb, comb_sum, target, res)
            comb.pop()
            comb_sum -= arr[i]


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        if not candidates:
            return []
        
        arr = sorted(set(candidates))

        # get index of last one which is less than or equal to target
        end = self.get_end(arr, target)
        if end == -1:
            return []
        end += 1
        start = 0
        
        comb = []
        res = []
        self.dfs(arr, start, end, comb, target, res)

        return res
    
    def get_end(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid
        
        if arr[right] <= target:
            return right
        if arr[left] <= target:
            return left
        return -1
    
    def dfs(self, arr, start, end, comb, target, res): # v1
        comb_sum = sum(comb)
        if comb_sum > target:
            return
        if comb_sum == target:
            res.append(sorted(comb))
            return
        
        for i in range(start, end):
            comb.append(arr[i])
            self.dfs(arr, i, end, comb, target, res)
            comb.pop()

    # 根据下层返回结果剪枝, not recommended
    def dfs(self, arr, start, end, comb, target, res): # v2
        comb_sum = sum(comb)
        if comb_sum > target:
            return 1
        if comb_sum == target:
            res.append(sorted(comb))
            return 0
        
        for i in range(start, end):
            comb.append(arr[i])
            overflow = self.dfs(arr, i, end, comb, target, res)
            comb.pop()
            if overflow:
                return 0
        
        return 0


# 剪枝版dfs
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        # write your code here
        if not candidates:
            return []
        
        arr = sorted(set(candidates))

        # get index of last one which is less than or equal to target
        end = self.get_end(arr, target)
        if end == -1:
            return []
        end += 1
        start = 0
        
        comb = []
        res = []
        self.dfs(arr, start, end, comb, 0, target, res)

        return res
    
    def get_end(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid
        
        if arr[right] <= target:
            return right
        if arr[left] <= target:
            return left
        return -1
    
    def dfs(self, arr, start, end, comb, comb_sum, target, res):
        if comb_sum == target:
            res.append(list(comb))
            return
        
        for i in range(start, end):
            comb.append(arr[i])
            comb_sum = sum(comb)
            # print(comb_sum)
            if comb_sum > target:
                comb.pop()
                return
            self.dfs(arr, i, end, comb, comb_sum, target, res)
            comb.pop()
