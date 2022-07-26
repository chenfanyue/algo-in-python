from typing import (
    List,
)

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        memo = {}
        visited = set()
        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in memo:
                    continue
                visited.add((i, j))
                r = self.dfs(matrix, i, j, memo, visited)
                visited.remove((i, j))
                res = max(res, r)
        
        return res

    def dfs(self, matrix, i, j, memo, visited):
        if (i, j) in memo:
            return memo[(i, j)]

        res = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = i + dx, j + dy
            if not self.valid(matrix, x, y, visited):
                continue
            if matrix[x][y] <= matrix[i][j]:
                continue
            visited.add((x, y))
            res = max(res, self.dfs(matrix, x, y, memo, visited) + 1)
            visited.remove((x, y))
        
        memo[(i, j)] = res
        return res

    def valid(self, matrix, x, y, visited):
        return 0 <= x < len(matrix) and \
            0 <= y < len(matrix[0]) and \
            (x, y) not in visited
