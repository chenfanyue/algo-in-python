from typing import (
    List,
)

# 坐标型dp，自顶向下
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        f = [[float('inf')] * m for _ in range(n)]

        if grid[0][0]:
            return -1
        f[0][0] = 0

        offset_x = [-1, -2, 1, 2]
        offset_y = [-2, -1, -2, -1]

        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for k in range(4):
                    x = i + offset_x[k]
                    y = j + offset_y[k]
                    if 0 <= x < n and 0 <= y < m:
                        f[i][j] = min(f[i][j], f[x][y] + 1)
        
        if f[n - 1][m - 1] == float('inf'):
            return -1
        return f[n - 1][m - 1]


# 自底向上dp, 注意初始化前要特判
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        f = [[float('inf')] * m for _ in range(n)]

        if grid[n - 1][m - 1]:
            return -1
        f[n - 1][m - 1] = 0

        offset_x = [-1, -2, 1, 2]
        offset_y = [2, 1, 2, 1]

        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if grid[i][j]:
                    continue
                for k in range(4):
                    x = i + offset_x[k]
                    y = j + offset_y[k]
                    if 0 <= x < n and 0 <= y < m:
                        f[i][j] = min(f[i][j], f[x][y] + 1)
        
        if f[0][0] == float('inf'):
            return -1
        return f[0][0]


# 单向bfs
from collections import deque

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        if grid[0][0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        offset_x = [-1, -2, 1, 2]
        offset_y = [2, 1, 2, 1]

        q = deque([(0, 0)])
        visited = {(0, 0): 0}

        while q:
            cur = q.popleft()
            if cur == (n - 1, m - 1):
                return visited[cur]
            
            for i in range(4):
                x = cur[0] + offset_x[i]
                y = cur[1] + offset_y[i]
                if self.visitable(grid, x, y, visited):
                    visited[(x, y)] = visited[cur] + 1
                    q.append((x, y))
        
        return -1
    
    def visitable(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        cond1 = 0 <= x < n and 0 <= y < m and not grid[x][y]
        cond2 = (x, y) not in visited
        return cond1 and cond2

