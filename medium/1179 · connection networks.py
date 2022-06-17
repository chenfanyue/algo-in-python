from typing import (
    List,
)

# bfs
class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        if not m or not m[0]:
            return 0
        
        n = len(m)
        connected = set()
        cnt = 0
        for i in range(n):
            if i not in connected:
                cnt += 1
                self.bfs(m, i, connected)
        
        return cnt
    
    def bfs(self, m, i, connected):
        connected.add(i)
        q = collections.deque([i])

        n = len(m)
        while q:
            i = q.popleft()

            for j in range(n):
                if m[i][j] and j not in connected:
                    connected.add(j)
                    q.append(j)


# dfs
class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        if not m or not m[0]:
            return 0
        
        n = len(m)
        connected = set()
        cnt = 0
        for i in range(n):
            if i not in connected:
                cnt += 1
                connected.add(i)
                self.dfs(m, i, connected)
        
        return cnt
    
    def dfs(self, m, i, connected):
        for j in range(len(m)):
            if m[i][j] and j not in connected:
                connected.add(j)
                self.dfs(m, j, connected)


# not recommended, disjoint-set, local function
class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        if not m or not m[0]:
            return 0
        
        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i: int, j: int):
            if find(i) != find(j):
                parent[find(i)] = find(j)
                parent[-1] -= 1
        
        n = len(m)
        parent = list(range(n))
        parent.append(n)

        for i in range(n):
            for j in range(i + 1, n):
                if m[i][j]:
                    union(i, j)
        
        return parent[-1]


# not recommended, disjoint-set
class Solution:
    """
    @param m: a matrix
    @return: the total number of friend circles among all the students
    """
    def find_circle_num(self, m: List[List[int]]) -> int:
        # Write your code here
        if not m or not m[0]:
            return 0
        
        cnt = n = len(m)
        parent = list(range(n))
        parent.append(cnt)

        for i in range(n):
            for j in range(i + 1, n):
                if m[i][j]:
                    self.union(i, j, parent)
        
        return parent[-1]

    def find(self, i: int, parent: List[int]) -> int:
        if parent[i] != i:
            parent[i] = self.find(parent[i], parent)
        return parent[i]
    
    def union(self, i: int, j: int, parent: List[int]):
        i_root = self.find(i, parent)
        j_root = self.find(j, parent)
        if i_root != j_root:
            parent[i_root] = j_root
            parent[-1] -= 1
