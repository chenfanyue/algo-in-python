from typing import (
    List,
    Set,
)

# 战略级剪枝
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start: str, end: str, word_dict: Set[str]) -> List[List[str]]:
        word_dict.update([start, end])
        distances = self.get_distances(end, word_dict)
        path = [start]
        res = []

        self.dfs(word_dict, distances, end, path, res)

        return res
    
    def get_distances(self, startoff, word_dict):
        distances = {startoff: 0}
        q = collections.deque([startoff])

        while q:
            cur = q.popleft()
            for neighbor in self.get_neighbors(cur, word_dict):
                if neighbor in distances:
                    continue
                distances[neighbor] = distances[cur] + 1
                q.append(neighbor)

        return distances
    
    def dfs(self, word_dict, distances, end, path, res):
        if path[-1] == end:
            res.append(list(path))
            return
        
        for neighbor in self.get_neighbors(path[-1], word_dict):
            # 战略级剪枝
            if distances[neighbor] != distances[path[-1]] - 1:
                continue
            path.append(neighbor)
            self.dfs(word_dict, distances, end, path, res)
            path.pop()

    def get_neighbors(self, word, word_dict):
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        neighbors = []

        for i in range(len(word)):
            for ch in alphers:
                if ch == word[i]:
                    continue
                word_new = word[:i] + ch + word[i + 1:]
                if word_new in word_dict:
                    neighbors.append(word_new)
        
        return neighbors


# 战术级剪枝
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start: str, end: str, word_dict: Set[str]) -> List[List[str]]:
        word_dict.update([start, end])
        visited = set([start])
        path = [start]
        res = []

        self.dfs(word_dict, end, visited, path, res)

        return res
    
    def dfs(self, word_dict, end, visited, path, res):
        # 战术级剪枝
        shortest = len(res[0]) if res else float('inf')
        if path[-1] == end:
            if len(path) == shortest:
                res.append(list(path))
            elif len(path) < shortest:
                res.clear()
                res.append(list(path))
            return
        else:
            if len(path) == shortest:
                return
        
        for neighbor in self.get_neighbors(path[-1], word_dict):
            if neighbor in visited:
                continue
            path.append(neighbor)
            visited.add(neighbor)
            self.dfs(word_dict, end, visited, path, res)
            path.pop()
            visited.remove(neighbor)

    def get_neighbors(self, word, word_dict):
        alphers = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        neighbors = []

        for i in range(len(word)):
            for ch in alphers:
                if ch == word[i]:
                    continue
                word_new = word[:i] + ch + word[i + 1:]
                if word_new in word_dict:
                    neighbors.append(word_new)
        
        return neighbors


