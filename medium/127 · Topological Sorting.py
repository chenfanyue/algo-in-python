"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

# bfs
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        indeg = {node: 0 for node in graph}
        for node in graph:
            for successor in node.neighbors:
                indeg[successor] += 1
        
        zero_indegree_nodes = [node for node in graph if indeg[node] == 0]
        q = collections.deque(zero_indegree_nodes)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for successor in node.neighbors:
                indeg[successor] -= 1
                if indeg[successor] == 0:
                    q.append(successor)
        
        return res


# bfs
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        indeg = dict()
        for node in graph:
            for successor in node.neighbors:
                indeg[successor] = indeg.get(successor, 0) + 1
        
        q = collections.deque()
        for node in graph:
            if node not in indeg:
                q.append(node)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for successor in node.neighbors:
                indeg[successor] -= 1
                if indeg[successor] == 0:
                    q.append(successor)
        
        return res


# bfs
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        indeg = dict()
        for node in graph:
            for successor in node.neighbors:
                indeg[successor.label] = indeg.get(successor.label, 0) + 1
        
        q = collections.deque()
        for node in graph:
            if node.label not in indeg:
                q.append(node)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for successor in node.neighbors:
                indeg[successor.label] -= 1
                if indeg[successor.label] == 0:
                    q.append(successor)
        
        return res
