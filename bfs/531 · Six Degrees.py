"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph node
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if not graph:
            return -1
        if s is t:
            return 0

        q = collections.deque(s.neighbors)
        visited = set(s.neighbors)
        distance = 0

        while q:
            distance += 1
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node is t:
                    return distance
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        return -1


# 双向bfs，处理当前层
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if not graph:
            return -1
        if s is t:
            return 0

        q1 = collections.deque([s])
        visited1 = set([s])
        q2 = collections.deque([t])
        visited2 = set([t])
        distance = -1

        while q1 and q2:
            distance += 1
            n = len(q1)
            for _ in range(n):
                node = q1.popleft()
                if node in visited2:
                    return distance
                for neighbor in node.neighbors:
                    if neighbor not in visited1:
                        visited1.add(neighbor)
                        q1.append(neighbor)
        
            distance += 1
            n = len(q2)
            for _ in range(n):
                node = q2.popleft()
                if node in visited1:
                    return distance
                for neighbor in node.neighbors:
                    if neighbor not in visited2:
                        visited2.add(neighbor)
                        q2.append(neighbor)
        
        return -1


# 双向bfs，处理下一层
"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if not graph:
            return -1
        if s is t:
            return 0

        q1 = collections.deque([s])
        visited1 = set([s])
        q2 = collections.deque([t])
        visited2 = set([t])
        distance = -1

        while q1 and q2:
            distance += 1
            res = self.bfs(q1, visited1, visited2, distance)
            if res > -1:
                return res
        
            distance += 1
            res = self.bfs(q2, visited2, visited1, distance)
            if res > -1:
                return res
        
        return -1

    def bfs(self, q1, visited1, visited2, distance):
        n = len(q1)
        for _ in range(n):
            node = q1.popleft()
            for neighbor in node.neighbors:
                if neighbor in visited2:
                    return distance + 1
                if neighbor not in visited1:
                    visited1.add(neighbor)
                    q1.append(neighbor)
        
        return -1

