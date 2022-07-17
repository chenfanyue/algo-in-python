from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        state = []
        visited = [False] * len(nums)
        res = []
        self.dfs(nums, visited, state, res)

        return res
    
    def dfs(self, nums, visited, state, res):
        if len(state) == len(nums):
            res.append(list(state))
        
        for i in range(len(visited)):
            if visited[i]:
                continue
            state.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, state, res)
            visited[i] = False
            state.pop()


class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        state = []
        visited = set()
        res = []
        self.dfs(nums, visited, state, res)

        return res
    
    def dfs(self, nums, visited, state, res):
        if len(state) == len(nums):
            res.append(list(state))
        
        for num in nums:
            if num in visited:
                continue
            state.append(num)
            visited.add(num)
            self.dfs(nums, visited, state, res)
            visited.remove(num)
            state.pop()


# simulate permutating, from first to last
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        nums = sorted(nums)
        res = []
        self.dfs(nums, 0, res)
        
        return res

    def dfs(self, nums, remaing_start, res):
        if remaing_start == len(nums) - 1:
            res.append(nums[:])
        
        for i in range(remaing_start, len(nums)):
            self.swap(nums, i, remaing_start)
            self.dfs(nums, remaing_start + 1, res)
            self.swap(nums, i, remaing_start)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# simulate permutating, from last to first
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]
        
        nums = sorted(nums)
        last = len(nums) - 1
        res = []
        self.dfs(nums, last, res)
        
        return res

    def dfs(self, nums, last, res):
        if last == 0:
            res.append(nums[:])
        
        for i in range(last + 1):
            self.swap(nums, i, last)
            self.dfs(nums, last - 1, res)
            self.swap(nums, i, last)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


# 模拟递归调用栈, v1
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        permutation = []
        permutations = []
        visited = set()

        stack = [(0, 0)]
        while stack:
            idx, count = stack.pop()

            if count == 0:
                if len(visited) == len(nums):
                    permutations.append(list(permutation))
                    continue
                    
                for i in range(len(nums)):
                    if nums[i] in visited:
                        continue
                    stack.append((i, 2))
                    stack.append((i + 1, 0))
                    stack.append((i, 1))

            if count == 1:
                permutation.append(nums[idx])
                visited.add(nums[idx])

            if count == 2:
                permutation.pop()
                visited.remove(nums[idx])

        return permutations


# 模拟递归调用栈, v2
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        permutations = []
        visited = [0] * len(nums)
        cnt = 0

        stack = [(0, 0)]
        while stack:
            idx, state = stack.pop()

            if state == 0:
                if cnt == len(nums):
                    permutations.append(list(permutation))
                    continue
                    
                for i in range(len(nums)):
                    if visited[i]:
                        continue
                    stack.append((i, 2))
                    stack.append((i + 1, 0))
                    stack.append((i, 1))

            if state == 1:
                permutation.append(nums[idx])
                visited[idx] = 1
                cnt += 1

            if state == 2:
                permutation.pop()
                visited[idx] = 0
                cnt -= 1

        return permutations


# 每次更新到下一个状态
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums[:]]
        
        nums = sorted(nums)
        res = []
        has_next = True
        
        while has_next:
            res.append(nums[:])
            has_next = self.next_permutation(nums)
        
        return res

    def next_permutation(self, nums):
        n = len(nums)

        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        if i == 0:
            return False
        
        j = n - 1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[j], nums[i-1] = nums[i-1], nums[j]
        
        self.swap_list(nums, i, n - 1)

        return True
    
    def swap_list(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


