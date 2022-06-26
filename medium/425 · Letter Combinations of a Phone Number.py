from typing import (
    List,
)

class Solution:
    """
    @param digits: A digital string
    @return: all possible letter combinations
             we will sort your return value in output
    """
    def letter_combinations(self, digits: str) -> List[str]:
        # write your code here
        if not digits:
            return []
        
        res = []
        path = []
        graph = self.get_graph()
        self.dfs(digits, 0, path, res, graph)

        return res
    
    def dfs(self, digits, i, path, res, graph):
        if i == len(digits):
            res.append(''.join(path))
            return

        for ch in graph.get(digits[i]):
            path.append(ch)
            self.dfs(digits, i + 1, path, res, graph)
            path.pop()

    def get_graph(self):
        return {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
