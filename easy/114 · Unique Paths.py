# dp
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def unique_paths(self, n: int, m: int) -> int:
        dp = [
            [0] * m
            for _ in range(n)
        ]

        for i in range(n):
            dp[i][0] = 1
        for j in range(m):
            dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[n - 1][m - 1]


# memo search, dfs
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def unique_paths(self, n: int, m: int) -> int:
        memo = {}
        return self.dfs(1, 1, n, m, memo)
    
    def dfs(self, i, j, n, m, memo):
        if i > n:
            return 0
        if j > m:
            return 0
        if i == n and j == m:
            return 1
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = self.dfs(i, j + 1, n, m, memo) + self.dfs(i + 1, j, n, m, memo)
        memo[(i, j)] = res

        return res
