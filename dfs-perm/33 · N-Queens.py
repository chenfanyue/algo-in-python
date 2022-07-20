from typing import (
    List,
)

class Solution:
    """
    @param n: The number of queens
    @return: All distinct solutions
             we will sort your return value in output
    """
    def solve_n_queens(self, n):
        if n <= 0:
            return []

        path = []
        res = []
        self.dfs(n, path, res)

        return res

    def dfs(self, n, path, res):
        if len(path) == n:
            res.append(self.translate(n, path))

        for j in range(n):
            if not self.valid(j, path):
                continue
            path.append(j)
            self.dfs(n, path, res)
            path.pop()

    def valid(self, col, path):
        row = len(path)
        for i, j in enumerate(path):
            if col == j:
                return False
            # if j - col == row - i or col - j == row - i:
            if abs(j - col) == row - i:
                return False
        
        return True

    def translate(self, n, path):
        res = []
        for v in path:
            tmp = ['.'] * n
            tmp[v] = 'Q'
            res.append(''.join(tmp))
        
        return res
