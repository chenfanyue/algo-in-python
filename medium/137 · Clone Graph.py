from lintcode import (
    UndirectedGraphNode,
)
from collections import deque


"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if not node:
            return None
        
        start = node

        nodes = self.bfs(node)

        mapping = self.do_mapping(nodes)
        
        for node in nodes:
            for neighbor in node.neighbors:
                neighbor_mapped = mapping[neighbor]
                mapping[node].neighbors.append(neighbor_mapped)
        
        return mapping[start]
    
    # bfs with queue
    def bfs(self, node):
        visited = set([node])
        q = deque([node])

        while q:
            node = q.popleft()

            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)
        
        return list(visited)

    # bfs without queue
    def bfs(self, node):
        visited = set([node])
        nodes = [node]

        i = 0
        while i < len(nodes):
            cur = nodes[i]
            i += 1
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes.append(neighbor)
        
        return nodes
    
    # dfs automatically, starting from node which has already been visited
        '''
        start = node
        visited = set([node])
        self.dfs(node, visited)
        nodes = list(visited)
        '''
    def dfs(self, node, visited):
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, visited)

    # dfs with stack
    def dfs(self, node):
        visited = set([node])
        stack = [node]
        neighbor_to_visit = {node: -1}

        while stack:
            cur = stack[-1]
            neighbor_to_visit[cur] += 1

            if (i := neighbor_to_visit[cur]) == len(cur.neighbors):
                stack.pop()
                continue
            
            if (neighbor := cur.neighbors[i]) in visited:
                continue
            
            visited.add(neighbor)
            stack.append(neighbor)
            neighbor_to_visit[neighbor] = -1
        
        return list(visited)

    def do_mapping(self, nodes):
        mapping = dict()
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        return mapping


# not recommended
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if not node:
            return None
        
        q = deque([node])
        mapping = {node: UndirectedGraphNode(node.label)}

        while q:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = UndirectedGraphNode(neighbor.label)
                    q.append(neighbor)
                mapping[cur].neighbors.append(mapping[neighbor])
        
        return mapping[node]


# not not recommended
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        # write your code here
        if not node:
            return None
        
        mapping = dict()

        return self.clone_node(node, mapping)

    def clone_node(self, node, mapping):
        if node in mapping:
            return mapping[node]
        
        clone = UndirectedGraphNode(node.label)
        mapping[node] = clone

        clone.neighbors = [self.clone_node(neighbor, mapping) for neighbor in node.neighbors]

        return clone

