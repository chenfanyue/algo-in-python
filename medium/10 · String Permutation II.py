from typing import (
    List,
)

# 基于交换每次确定一位
class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = list(s)
        res = []
        
        self.dfs(arr, 0, res)

        return res

    def dfs(self, arr, i, res):
        if i == len(arr):
            res.append(''.join(arr))
            return
        
        visited = set()
        for j in range(i, len(arr)):
            if arr[j] in visited:
                continue
            visited.add(arr[j])
            self.swap(i, j, arr)
            self.dfs(arr, i + 1, res)
            self.swap(i, j, arr)

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]


class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = list(s)
        res = []
        
        self.dfs(arr, 0, res)

        return res

    def dfs(self, arr, i, res):
        if i == len(arr):
            res.append(''.join(arr))
            return
        
        for j in range(i, len(arr)):
            if not self.can_swap(arr, i, j):
                continue
            self.swap(i, j, arr)
            self.dfs(arr, i + 1, res)
            self.swap(i, j, arr)
    
    def can_swap(self, arr, start, j):
        for k in range(start, j):
            if arr[k] == arr[j]:
                return False
        return True

    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]


# 累积型动态状态量，每次增加一位, 伴生数据结构的使用
class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = sorted(s)
        visited = [False] * len(arr)
        path = []
        res = []
        self.dfs(arr, visited, path, res)

        return res

    def dfs(self, arr, visited, path, res):
        if len(path) == len(arr):
            res.append(''.join(path))
            return
        
        for i in range(len(arr)):
            if visited[i]:
                continue
            # 在当前层去重
            if i and not visited[i - 1] and arr[i] == arr[i - 1]:
                continue
            path.append(arr[i])
            visited[i] = True
            self.dfs(arr, visited, path, res)
            path.pop()
            visited[i] = False


class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = sorted(s)
        path = []
        res = []
        visited = set() # index
        self.dfs(arr, path, visited, res)

        return res

    def dfs(self, arr, path, visited, res):
        if len(path) == len(arr):
            res.append(''.join(path))
            return
        
        for j in range(len(arr)):
            if j in visited:
                continue
            if j and j - 1 not in visited and arr[j] == arr[j - 1]:
                continue
            path.append(arr[j])
            visited.add(j)
            self.dfs(arr, path, visited, res)
            path.pop()
            visited.remove(j)


class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = sorted(s)
        path = []
        res = []
        visited = set() # index
        self.dfs(arr, 0, path, visited, res)

        return res

    def dfs(self, arr, i, path, visited, res): # v1
        if i == len(arr):
            res.append(''.join(path))
            return
        
        for j in range(len(arr)):
            if j in visited:
                continue
            if j and j - 1 not in visited and arr[j] == arr[j - 1]:
                continue
            path.append(arr[j])
            visited.add(j)
            self.dfs(arr, i + 1, path, visited, res)
            path.pop()
            visited.remove(j)


# 累积型动态状态量，每次增加一位
class Solution:
    """
    @param s: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, s: str) -> List[str]:
        # write your code here
        if not s:
            return ['']
        
        arr = sorted(s)
        path = []
        res = []
        path_visited = set() # index
        self.dfs(arr, 0, path, path_visited, res)

        return res

    def dfs(self, arr, i, path, path_visited, res): # v1
        if i == len(arr):
            res.append(''.join(path))
            return
        
        local_visited = set() # value
        for j in range(len(arr)):
            if j in path_visited:
                continue
            if arr[j] in local_visited:
                continue
            local_visited.add(arr[j])
            path.append(arr[j])
            path_visited.add(j)
            self.dfs(arr, i + 1, path, path_visited, res)
            path.pop()
            path_visited.remove(j)

    def dfs(self, arr, i, path, path_visited, res): # v2
        if i == len(arr):
            res.append(''.join(path))
            return
        
        prev_try = None
        for j in range(len(arr)):
            if j in path_visited:
                continue
            if arr[j] == prev_try:
                continue
            prev_try = arr[j]
            path.append(arr[j])
            path_visited.add(j)
            self.dfs(arr, i + 1, path, path_visited, res)
            path.pop()
            path_visited.remove(j)


# 数据结构的重构，得到组合型数据结构
# arr = [
#     {'val': ch, 'visited': False}
#     for ch in s
# ]
# arr.sort(key=lambda e: e['val'])
