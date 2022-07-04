class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        
        memo = {}
        return self.dfs(n, memo)

    def dfs(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in memo:
            return memo[n]

        res = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
        memo[n] = res

        return res


# dp-coordiante
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        # elastic initialization
        for i in range(min(3, n + 1)):
            dp[i] = i

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]
