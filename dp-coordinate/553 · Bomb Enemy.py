from typing import (
    List,
)

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def max_killed_enemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        up = [[0] * m for _ in range(n)]
        down = [[0] * m for _ in range(n)]
        left = [[0] * m for _ in range(n)]
        right = [[0] * m for _ in range(n)]

        # up
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        up[i][j] += 1
                    if i > 0:
                        up[i][j] += up[i - 1][j]

        # down
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                    if i < n - 1:
                        down[i][j] += down[i + 1][j]

        # left
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        left[i][j] += 1
                    if j > 0:
                        left[i][j] += left[i][j - 1]

        # right
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        right[i][j] += 1
                    if j < m - 1:
                        right[i][j] += right[i][j + 1]
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        return res
