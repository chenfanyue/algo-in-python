from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        dp = [
            [0] * m
            for _ in range(n)
        ]

        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[n-1][m-1]


class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        dp = [
            [0] * m
            for _ in range(2)
        ]

        old = now = 0
        for i in range(n):
            old = now
            now = 1 - old
            for j in range(m):
                dp[now][j] = float('inf')
                if i == 0 and j == 0:
                    dp[now][0] = grid[i][j]
                    continue
                if i > 0:
                    dp[now][j] = min(dp[now][j], dp[old][j] + grid[i][j])
                if j > 0:
                    dp[now][j] = min(dp[now][j], dp[now][j - 1] + grid[i][j])
        
        return dp[now][m-1]


# hwo to print the path
# 利用回溯链，钩子的方向为贡献值为1的方向
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        dp = [
            [0] * m
            for _ in range(n)
        ]
        hook = [[0] * m for _ in range(n)] # 0 from above, 1 from left

        dp[0][0] = grid[0][0]
        hook[0][0] = -1 # for in case of dynamic array
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            hook[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                if dp[i][j-1] < dp[i-1][j]:
                    hook[i][j] = 1
        
        path = [[0, 0] for _ in range(n + m - 1)]
        i, j = n -1, m - 1
        for p in range(n + m - 2, -1, -1):
            path[p][0], path[p][1] = i, j
            if hook[i][j]:
                j -= 1
            else:
                i -= 1
        
        print(path)

