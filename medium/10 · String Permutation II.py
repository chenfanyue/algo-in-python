from typing import (
    List,
)

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

