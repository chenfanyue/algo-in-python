from typing import (
    List,
)

class Solution:
    """
    @param obstacle_grid: A list of lists of integers
    @return: An integer
    """
    def unique_paths_with_obstacles(self, obstacle_grid: List[List[int]]) -> int:
        # write your code here
        if not obstacle_grid or not obstacle_grid[0]:
            return 0
        
        n, m = len(obstacle_grid), len(obstacle_grid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            if obstacle_grid[i][0]:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacle_grid[0][j]:
                break
            dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacle_grid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[n - 1][m - 1]
