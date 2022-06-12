from typing import (
    List,
)

# bfs with set
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0

        visited = set()
        cnt = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    cnt += 1
        
        return cnt
    
    def bfs(self, grid, i, j, visited):
        MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited.add((i, j))
        q = collections.deque([(i, j)])

        while q:
            i, j = q.popleft()
            for move in MOVES:
                delta_x, delta_y = move
                x, y = i + delta_x, j + delta_y
                if self.is_virgin_island(grid, x, y, visited):
                    visited.add((x, y))
                    q.append((x, y))
    
    def is_virgin_island(self, grid, x, y, visited):
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        b = (x, y) not in visited
        return a and grid[x][y] and b


# bfs with 2d-array
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    self.bfs(grid, i, j, visited)
                    cnt += 1
        
        return cnt
    
    def bfs(self, grid, i, j, visited):
        MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited[i][j] = True
        qx = collections.deque([i])
        qy = collections.deque([j])

        while qx:
            i, j = qx.popleft(), qy.popleft()
            for move in MOVES:
                delta_x, delta_y = move
                x, y = i + delta_x, j + delta_y
                if self.is_virgin_island(grid, x, y, visited):
                    visited[x][y] = True
                    qx.append(x)
                    qy.append(y)
    
    def is_virgin_island(self, grid, x, y, visited):
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] and not visited[x][y]


# dfs
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        # print(sys.version)
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        unvisited = [[True] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and unvisited[i][j]:
                    cnt += 1
                    self.dfs(grid, i, j, unvisited)
        
        return cnt
    
    def dfs(self, grid, i, j, unvisited):
        # 抵达一个深空尽头就会自然返回 
        MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        unvisited[i][j] = False

        for move in MOVES:
            delta_x, delta_y = move
            x, y = i + delta_x, j + delta_y
            if self.is_virgin_island(grid, x, y, unvisited):
                self.dfs(grid, x, y, unvisited)

    def dfs(self, grid, i, j, unvisited):
        # version 2, recommended
        if not self.is_virgin_island(grid, i, j, unvisited):
            return
        
        MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        unvisited[i][j] = False

        for move in MOVES:
            delta_x, delta_y = move
            x, y = i + delta_x, j + delta_y
            self.dfs(grid, x, y, unvisited)

    def is_virgin_island(self, grid, x, y, visited):
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] and unvisited[x][y]


# UnionFind并查集
#
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        # print(sys.version)
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cnt += 1
        
        union_find = UnionFind(n * m, cnt)
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if i + 1 < n and grid[i+1][j]:
                        union_find.union(i * m + j, i * m + j + m)
                    if j + 1 < m and grid[i][j+1]:
                        union_find.union(i * m + j, i * m + j + 1)
        
        return union_find.get_cnt()
    
class UnionFind:
    def __init__(self, n, cnt):
        self.arr = [i for i in range(n)]
        self.cnt = cnt
    
    def find_root(self, i):
        if self.arr[i] == i:
            return i
        self.arr[i] = self.find_root(self.arr[i])
        return self.arr[i]
    
    def union(self, a, b):
        a_root = self.find_root(a)
        b_root = self.find_root(b)
        if a_root != b_root:
            self.arr[a_root] = b_root
            self.cnt -= 1
    
    def get_cnt(self):
        return self.cnt
