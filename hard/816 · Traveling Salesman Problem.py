from typing import (
    List,
)


class Result:
    def __init__(self):
        self.min_cost = float('inf')


# 剪枝版dfs, 级联dict存储邻接矩阵
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


# state compression dynamic programming, recommended, 物理下标体系
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        graph = self.get_graph(n, roads)
        table = [
            [float('inf') for _ in range(n)]
            for _ in range(1 << n)
        ]
        # start from city 0
        table[1][0] = 0

        for state in range(2, 1 << n):
            for v in range(1, n):
                if state & (1 << v):
                    prev_state = state ^ (1 << v)
                    for u in range(n):
                        if prev_state & (1 << u) and v in graph[u]:
                            new_cost = table[prev_state][u] + graph[u][v]
                            if new_cost < table[state][v]:
                                table[state][v] = new_cost
        
        last_state = table[(1 << n) - 1]
        
        return min(last_state)
    

    def get_graph(self, n, roads):
        # construct adjacency table
        graph = [
            dict()
            for _ in range(n)
        ]
        
        for a, b, weight in roads:
            weight_existed = graph[a - 1].get(b - 1, float('inf'))
            if weight < weight_existed:
                graph[a - 1][b - 1] = weight
                graph[b - 1][a - 1] = weight
        
        return graph


# state compression dynamic programming, 逻辑下标体系
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        graph = self.get_graph(n, roads)
        table = {
            state: {city: float('inf') for city in range(n, 0, -1)}
            for state in range(1 << n)
        }
        # start from city 1
        table[1][1] = 0

        for state in range(1 << n):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)):
                    # prev_state = state - pow(2, i - 1)
                    prev_state = state ^ (1 << (i - 1))
                    for j in range(1, n + 1):
                        if prev_state & (1 << (j - 1)):
                            if (val := table[prev_state][j] + graph[j][i]) < table[state][i]:
                                table[state][i] = val
        
        last_state = table[(1 << n) - 1]
        
        return min(last_state[city] for city in last_state)
    

    def get_graph(self, n, roads):
        # construct adjacency matrix
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


# state compression dynamic programming, 逻辑下标体系
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        graph = self.get_graph(n, roads)
        table = {
            state: {city: float('inf') for city in range(1, n + 1)}
            for state in range(1 << n)
        }
        # start from city 1
        table[1][1] = 0

        for state in range(1 << n):
            for i in range(2, n + 1):
                if state & (1 << (i - 1)):
                    prev_state = state ^ (1 << (i - 1))
                    for j in range(1, n + 1):
                        if prev_state & (1 << (j - 1)):
                            table[state][i] = min(table[state][i], table[prev_state][j] + graph[j][i])
        
        last_state = table[(1 << n) - 1]
        
        return min(val for val in last_state.values())
    

    def get_graph(self, n, roads):
        # construct adjacency matrix
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        
        for a, b, weight in roads:
            if weight < graph[a][b]:
                graph[a][b] = weight
                graph[b][a] = weight
        
        return graph


# state compression dynamic programming, 从构图、状态推导表、状态推导，全程物理下标体系
class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        # Write your code here
        graph = self.get_graph(n, roads)
        table = [
            [float('inf') for _ in range(n)]
            for _ in range(1 << n)
        ]
        # start from city 0
        table[1][0] = 0

        for state in range(2, 1 << n):
            for v in range(1, n):
                if state & (1 << v):
                    prev_state = state ^ (1 << v)
                    for u in range(n):
                        # if prev_state & (1 << u):
                        table[state][v] = min(table[state][v], table[prev_state][u] + graph[u][v])
        
        last_state = table[(1 << n) - 1]
        
        return min(last_state)
    

    def get_graph(self, n, roads):
        # construct adjacency matrix
        graph = [
            [float('inf') for _ in range(n)]
            for _ in range(n)
        ]
        
        for a, b, weight in roads:
            if weight < graph[a - 1][b - 1]:
                graph[a - 1][b - 1] = weight
                graph[b - 1][a - 1] = weight
        
        return graph




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




