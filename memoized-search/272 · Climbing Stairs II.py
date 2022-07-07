# memoized search
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n == 0:
            return 1
        
        memo = {}

        return self.dfs(n, memo)
    
    def dfs(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        
        if n in memo:
            return memo[n]
        
        res = self.dfs(n - 1, memo) + \
                self.dfs(n - 2, memo) + \
                self.dfs(n - 3, memo)
        
        memo[n] = res
        return res


# dp
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[n]
