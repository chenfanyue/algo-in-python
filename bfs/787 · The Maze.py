from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def has_path(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return False

        n, m = len(maze), len(maze[0])
        q = collections.deque([(start[0], start[1])])
        visited = set([(start[0], start[1])])

        while q:
            cur = q.popleft()
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return True
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = cur[0] + dx, cur[1] + dy
                while 0 <= x < n and 0 <= y < m and maze[x][y] == 0:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if (x, y) not in visited:
                    visited.add((x, y))
                    q.append((x, y))
        
        return False
