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

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        DIRECTIONS = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        dest = (destination.x, destination.y)
        visited = {(source.x, source.y): 0}
        q = collections.deque([(source.x, source.y)])

        while q:
            x, y = q.popleft()
            if (x, y) == dest:
                return visited[(x, y)]
            
            for dx, dy in DIRECTIONS:
                neighbor = (x + dx, y + dy)
                if self.jumpable(grid, neighbor, visited):
                    visited[neighbor] = visited[(x, y)] + 1
                    q.append(neighbor)
        
        return -1
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] == False and neighbor not in visited


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        DIRECTIONS = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        dest = (destination.x, destination.y)
        level = 0
        visited = set([(source.x, source.y)])
        q = collections.deque([(source.x, source.y)])

        while q:
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                if (x, y) == dest:
                    return level
                
                for dx, dy in DIRECTIONS:
                    neighbor = (x + dx, y + dy)
                    if self.jumpable(grid, neighbor, visited):
                        visited.add(neighbor)
                        q.append(neighbor)
            level += 1
        
        return -1
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] == False and neighbor not in visited


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        DIRECTIONS = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        dest = (destination.x, destination.y)
        level = 0
        if (source.x, source.y) == dest:
            return level
        visited = set([(source.x, source.y)])
        q = collections.deque([(source.x, source.y)])

        while q:
            level += 1
            n = len(q)
            for _ in range(n):
                x, y = q.popleft()
                
                for dx, dy in DIRECTIONS:
                    neighbor = (x + dx, y + dy)
                    if not self.jumpable(grid, neighbor, visited):
                        continue
                    if neighbor == dest:
                        return level
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return -1
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] == False and neighbor not in visited


# do not use this version, creating so many objects, awful
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        DIRECTIONS = [
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        ]
        q = collections.deque()
        q.append(source)
        visited = dict()
        visited[(source.x, source.y)] = 0

        while q:
            cur = q.popleft()
            if (cur.x, cur.y) == (destination.x, destination.y):
                return visited[(cur.x, cur.y)]
            
            for (dx, dy) in DIRECTIONS:
                neighbor = Point(cur.x + dx, cur.y + dy)
                if self.jumpable(grid, neighbor, visited):
                    visited[(neighbor.x, neighbor.y)] = visited[(cur.x, cur.y)] + 1
                    q.append(neighbor)
        
        return -1
        
    def jumpable(self, grid, neighbor, visited):
        x, y = neighbor.x, neighbor.y
        a = -1 < x < len(grid) and -1 < y < len(grid[0])
        return a and grid[x][y] == False and (neighbor.x, neighbor.y) not in visited
