from typing import (
    List,
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

# 单向bfs
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        if not grid or not grid[0]:
            return -1
        if grid[source.x][source.y] or grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        
        DIRECTIONS = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        dest = (destination.x, destination.y)
        distance = 0
        q = collections.deque([(source.x, source.y)])
        visited = set([(source.x, source.y)])

        while q:
            distance += 1
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                
                for dx, dy in DIRECTIONS:
                    neighbor = (x + dx, y + dy)
                    if not self.jumpable(grid, neighbor, visited):
                        continue
                    if neighbor == dest:
                        return distance
                    q.append(neighbor)
                    visited.add(neighbor)
        
        return -1
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor
        inbound = -1 < x < len(grid) and -1 < y < len(grid[0])
        return inbound and grid[x][y] == False and neighbor not in visited


# 双向bfs
DIRECTIONS = [
    (1, 2), (1, -2), (-1, 2), (-1, -2),
    (2, 1), (2, -1), (-2, 1), (-2, -1)
]

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        if not grid or not grid[0]:
            return -1
        if grid[source.x][source.y] or grid[destination.x][destination.y]:
            return -1
        if (source.x, source.y) == (destination.x, destination.y):
            return 0
        
        forward_q = collections.deque([(source.x, source.y)])
        forward_visited = set([(source.x, source.y)])
        backward_q = collections.deque([(destination.x, destination.y)])
        backward_visited = set([(destination.x, destination.y)])
        distance = 0

        while forward_q and backward_q:
            distance += 1
            if self.meeted(grid, forward_q, forward_visited, backward_visited):
                return distance
            
            distance += 1
            if self.meeted(grid, backward_q, backward_visited, forward_visited):
                return distance
        
        return -1

    def meeted(self, grid, q, visited, opposite_visited):
        n = len(q)
        for _ in range(n):
            x, y = q.popleft()
            
            for dx, dy in DIRECTIONS:
                neighbor = (x + dx, y + dy)
                if not self.jumpable(grid, neighbor, visited):
                    continue
                if neighbor in opposite_visited:
                    return True
                q.append(neighbor)
                visited.add(neighbor)
    
        return False
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor
        inbound = -1 < x < len(grid) and -1 < y < len(grid[0])
        return inbound and grid[x][y] == False and neighbor not in visited
