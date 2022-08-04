from typing import (
    List,
)

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0]:
            return -1

        visited = {(start[0], start[1]): 0}
        for i in range(4):
            res = self.dfs(maze, (start[0], start[1]), i, (destination[0], destination[1]), visited)
            if res != -1:
                return res
        
        return -1

    def dfs(self, maze, start, direction, end, visited):
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dx, dy = DIRECTIONS[direction]
        next_x, next_y = start[0] + dx, start[1] + dy

        if start == end and self.hit_wall(maze, next_x, next_y):
            return visited[end]

        dirs = [direction] + [i for i in range(4) if i != direction]
        for i in dirs:
            dx, dy = DIRECTIONS[i]
            x, y = start[0] + dx, start[1] + dy
            if self.valid(maze, x, y, visited):
                visited[(x, y)] = visited[start] + 1
                res = self.dfs(maze, (x, y), i, end, visited)
                if res != -1:
                    return res
                visited.pop((x, y))
        
        return -1

    def valid(self, maze, x, y, visited):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and \
            not maze[x][y] and \
            (x, y) not in visited

    def hit_wall(self, maze, x, y):
        return not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or \
            maze[x][y]
