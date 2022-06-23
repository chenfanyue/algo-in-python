from typing import (
    List,
)


class Result:
    def __init__(self):
        self.min_cost = float('inf')


# 剪枝版dfs
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        res = Result()
        graph = self.get_graph(n, roads)
        visited = set([1])
        path = [1]
        self.dfs(1, 0, n, visited, path, graph, res)

        return res.min_cost
    
    def dfs(self, latest, total_cost, n, visited, path, graph, res):
        if len(visited) == n:
            if total_cost < res.min_cost:
                res.min_cost = total_cost
            return
        
        for to in range(1, n + 1):
            if to in visited:
                continue
            if self.has_shorter_path(path, to, graph):
                continue
            visited.add(to)
            path.append(to)
            self.dfs(to, total_cost + graph[latest][to], n, visited, path, graph, res)
            path.pop()
            visited.remove(to)

    def get_graph(self, n, roads):
        # graph = dict()
        # for i in range(1, n + 1):
        #     graph[i] = dict()
        #     for j in range(1, n + 1):
        #         graph[i][j] = float('inf')
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        
        for a, b, weight in roads:
            if weight < graph[a][b]:
                graph[a][b] = weight
                graph[b][a] = weight
        
        return graph

    def has_shorter_path(self, path, to, graph):
        # no road between path[-1] and to
        if graph[path[-1]][to] == float('inf'):
            return True
        
        # path[0] to the city to visit has a shorter path
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][to] > \
                graph[path[i - 1]][path[-1]] + graph[path[i]][to]:
                return True
        
        return False


# brute dfs, not recommended
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        res = Result()
        graph = self.get_graph(n, roads)
        visited = set([1])
        self.dfs(1, 0, n, visited, graph, res)

        return res.min_cost
    
    def dfs(self, city, total_cost, n, visited, graph, res):
        if len(visited) == n:
            if total_cost < res.min_cost:
                res.min_cost = total_cost
            return
        
        for i in range(1, n + 1):
            if i in visited:
                continue
            visited.add(i)
            self.dfs(i, total_cost + graph[city][i], n, visited, graph, res)
            visited.remove(i)

    def get_graph(self, n, roads):
        # graph = dict()
        # for i in range(1, n + 1):
        #     graph[i] = dict()
        #     for j in range(1, n + 1):
        #         graph[i][j] = float('inf')
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        
        for a, b, weight in roads:
            if weight < graph[a][b]:
                graph[a][b] = weight
                graph[b][a] = weight
        
        return graph




