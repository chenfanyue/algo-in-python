from typing import (
    List,
)

# topological sort, topological order, bfs
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if num_courses == 1:
            return True
        
        graph = [[] for _ in range(num_courses)]
        indgree = [0] * num_courses

        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            indgree[node_in] += 1
        
        topo_order = []
        q = collections.deque()

        for i in range(num_courses):
            if indgree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo_order.append(node)
            for successor in graph[node]:
                indgree[successor] -= 1
                if indgree[successor] == 0:
                    q.append(successor)
        
        # print(topo_order)
        return len(topo_order) == num_courses


# bfs
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if num_courses == 1:
            return True
        
        graph = [[] for _ in range(num_courses)]
        indgree = [0] * num_courses

        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            indgree[node_in] += 1
        
        topo_cnt = 0
        q = collections.deque()

        for i in range(num_courses):
            if indgree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo_cnt += 1
            for successor in graph[node]:
                indgree[successor] -= 1
                if indgree[successor] == 0:
                    q.append(successor)
        
        return topo_cnt == num_courses


# dfs
class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if num_courses == 1:
            return True
        
        edges = [[] for _ in range(num_courses)]
        states = [0] * num_courses
        # indeg = [0] * num_courses

        for node_in, node_out in prerequisites:
            edges[node_out].append(node_in)
            # indeg[node_in] += 1
        
        stack = []
        for i in range(num_courses):
            # if indeg[i] > 0:
            #     continue
            if states[i] == 0:
                self.dfs(i, edges, states, stack)
            if states[i] == 1:
                break
            # if states[i] == 1:
            #     return False
        
        return len(stack) == num_courses
        # return True
    
    def dfs(self, i, edges, states, stack):
        states[i] = 1
        for successor in edges[i]:
            if states[successor] == 0:
                self.dfs(successor, edges, states, stack)
                # if states[successor] == 1:
                #     return
            if states[successor] == 1:
                return
        states[i] = 2
        stack.append(i)
